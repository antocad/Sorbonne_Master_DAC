#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:10:06 2020

@author: 3670631
"""
from TextRepresenter import PorterStemmer
import math

class IndexerSimple:
    def __init__(self, collection):
        self.index = dict()
        self.indexinv = dict()
        self.index_tfidf = dict()
        self.indexinv_tfidf = dict()
        self.collection=collection
        self.N = len(self.collection)
        self.indexation()
    
    def inverse_index(self, index):
        res = dict()
        for doc,mots in index.items():
            for mot,occ in mots.items():
                if mot not in res:
                    res[mot]={doc:occ}
                else:
                    res[mot][doc] = occ
        return res

    def indexation(self):
        for doc in self.collection.values():
            porter = PorterStemmer().getTextRepresentation(doc.text)
            self.index[doc.identifiant] = porter
        self.indexinv = self.inverse_index(self.index)
        #calcul du tfidf
        for doc, occurs in self.index.items():
            self.index_tfidf[doc] = dict()
            for mot, nb in occurs.items():
                tf = nb
                df = len(self.indexinv[mot])
                idf = math.log((1+self.N)/(1 + df))
                self.index_tfidf[doc][mot] = tf*idf
        self.indexinv_tfidf = self.inverse_index(self.index_tfidf)
        
    def getTfsForDoc(self,idDoc):
        return self.index[idDoc]
    
    def getTfIDFsForDoc(self,idDoc):
        return self.index_tfidf[idDoc]
    
    def getTfsForStem(self,stem):
        return self.indexinv[stem]
    
    def getTfIDFsForStem(self,stem):
        return self.indexinv_tfidf[stem]
    
    def getIDFsForStem(self,stem):
        df = len(self.indexinv[stem])
        return math.log((1+self.N)/(1 + df))
    
    def getStrDoc(self,idDoc):
        return self.collection[idDoc].text