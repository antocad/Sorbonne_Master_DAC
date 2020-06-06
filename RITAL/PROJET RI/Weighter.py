#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:43:40 2020

@author: 3670631
"""
from collections import Counter
from TextRepresenter import PorterStemmer
import math

class Weighter:
    def __init__(self, indexer):
        self.indexer = indexer

    def getWeightsForDoc(self, idDoc):
        raise NotImplementedError

    def getWeightsForStem(self, stem):
        raise NotImplementedError

    def getWeightsForQuery(self, query):
        raise NotImplementedError


class Weighter1(Weighter):
    """
    w_t,d = tf_t,d et w_t,q = 1 si t appartient à q, 0 sinon
    """
    def getWeightsForDoc(self, idDoc):
        return self.indexer.getTfsForDoc(idDoc)

    def getWeightsForStem(self, stem):
        return self.indexer.getTfsForStem(stem)

    def getWeightsForQuery(self, query):
        return dict(Counter(set(PorterStemmer().getTextRepresentation(query).keys())))

class Weighter2(Weighter1):
    """
    w_t,d = tf_t,d et w_t,q = tf_t,q
    """
    def getWeightsForQuery(self, query):
        return PorterStemmer().getTextRepresentation(query)

class Weighter3(Weighter1):
    """
    w_t,d = tf_t,d et w_t,q = idf_t
    """
    def getWeightsForQuery(self, query):
        res=dict()
        req_stem = set(PorterStemmer().getTextRepresentation(query).keys())
        for stem in req_stem:
            res[stem]=self.indexer.getIDFsForStem(stem)
        return res

class Weighter4(Weighter3):
    """
    w_t,d = 1+log(tf_t,d) et w_t,q = idf_t
    """
    def getWeightsForDoc(self, idDoc):
        res = dict()
        for stem,v in self.indexer.getTfsForDoc(idDoc).items():
            res[stem] = 1+math.log(v)
        return res


    def getWeightsForStem(self, stem):
        res = dict()
        for doc,v in self.indexer.getTfsForStem(stem).items():
            res[doc] = 1+math.log(v)
        return res

class Weighter5(Weighter):
    """
    w_t,d = 1+log(tf_t,d)*idf_t et w_t,q = 1+log(tf_t,q)*idf_t
    """
    def getWeightsForDoc(self, idDoc):
        res = dict()
        for stem,v in self.indexer.getTfsForDoc(idDoc).items():
            res[stem] = (1+math.log(v)) * self.indexer.getIDFsForStem(stem)
        return res


    def getWeightsForStem(self, stem):
        res = dict()
        for doc,v in self.indexer.getTfsForStem(stem).items():
            res[doc] = (1+math.log(v)) * self.indexer.getIDFsForStem(stem)
        return res

    def getWeightsForQuery(self, query):
        res=dict()
        req_stem = dict(Counter(PorterStemmer().getTextRepresentation(query).keys()))
        for stem in req_stem:
            res[stem]=(1 + math.log(req_stem[stem]))*self.indexer.getIDFsForStem(stem)
        return res
