#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:49:04 2020

@author: 3670631
"""

import math
from TextRepresenter import PorterStemmer
from collections import Counter

class IRModel:
    def __init__(self,indexer):
        self.indexer = indexer

    def getScores(self,query):
        raise NotImplementedError

    def getRanking(self,query):
        return sorted(self.getScores(query).items(), key = lambda c : c[1], reverse=True)



class Vectoriel(IRModel):
    def __init__(self, weighter, normalized):
        """
        si normalized est à True calcul avec score cosinus, si False produit scalaire
        """
        self.weighter = weighter
        self.normalized = normalized
        self.normeDoc = dict()
        if self.normalized:
            #car calcul score cosinus
            self.calculNormeDoc()

    def calculNormeDoc(self):
        """calcul de la norme des docs"""
        for doc in self.weighter.indexer.collection.keys():
            norm_doc = 0
            for mot ,occ in self.weighter.getWeightsForDoc(doc).items():
                norm_doc += occ**2
            norm_doc=math.sqrt(norm_doc)
            self.normeDoc[doc]=norm_doc

    def getScores(self, query):
        if (self.normalized):
            return self.scoreModeleCosinus(query)
        else:
            return self.scoreModeleVect(query)

    def scoreModeleCosinus(self,req):
        res = dict()
        req_stem = self.weighter.getWeightsForQuery(req)

        norm_q = 0
        #calcule de la norme de la requete
        for stem, occ in req_stem.items():
            norm_q+=occ**2
        norm_q=math.sqrt(norm_q)

        prod_scalaire = self.scoreModeleVect(req)
        for doc, prod in prod_scalaire.items():
            norm_doc = self.normeDoc[doc]
            res[doc]=prod/(norm_q+norm_doc)

        return res

    def scoreModeleVect(self,req):
        res = dict()
        req_stem = self.weighter.getWeightsForQuery(req)

        for stem, occ_stem in req_stem.items():
            docs = self.weighter.getWeightsForStem(stem)
            for doc, occ in docs.items():
                if(doc not in res):
                    res[doc]=occ_stem*occ
                else:
                    res[doc]+=occ_stem*occ
        return res

class Okapi(IRModel):
    def __init__(self,indexer, b=0.75, k1=1.2):
        self.indexer = indexer
        self.collection = self.indexer.collection
        self.avgdl = self.calculAvgdl()
        self.b = b
        self.k1 = k1

    def calculAvgdl(self):
        somme=0
        for id, doc in self.collection.items():
            somme += doc.getNbMot()
        return somme / len(self.collection)

    def getScores(self, query):
        res = dict()
        req_stem = PorterStemmer().getTextRepresentation(query).keys()
        for id,doc in self.collection.items() :
            score = 0
            for stem in req_stem:
                stem_occ = self.indexer.getTfsForDoc(id)
                if (stem in stem_occ):
                    lenD = doc.getNbMot()
                    idf = self.indexer.getIDFsForStem(stem)
                    tf = stem_occ[stem]
                    score += idf * (tf/(tf+self.k1 * (1-self.b+self.b*(lenD/self.avgdl))))
            res[id]=score
        return res

class ModeleLangue(IRModel):
    def __init__(self,indexer,param=0.8):
        self.indexer = indexer
        self.collection = self.indexer.collection
        self.parm = param
        self.nbmotcorpus = sum([doc.getNbMot() for doc in self.collection.values()])

    def getScores(self, query):
        res = dict()
        req_stem = PorterStemmer().getTextRepresentation(query)
        for id,doc in self.collection.items() :
            score = 0
            for stem,occ in req_stem.items():
                stem_occ = self.indexer.getTfsForDoc(id)
                tmp1 = (1-self.parm)
                tmp2 = self.parm
                if (stem in stem_occ):
                    tmp1 *= (stem_occ[stem]/doc.getNbMot())
                else : 
                    tmp1 = 0
                if (stem in self.indexer.indexinv):
                    doc_occ = self.indexer.getTfsForStem(stem)
                    tmp2 *= (sum(doc_occ.values())/self.nbmotcorpus)
                else : 
                    tmp2 = 0
                if(tmp1+tmp2 != 0):
                    score += occ*math.log(tmp1+tmp2)
            res[id]=score
        return res
