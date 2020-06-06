#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class EvalIRModel:
    def __init__(self, model):
        self.ranking = None
        self.model = model

    def evaluateQuery(self, query, scorer):
        """
        on retourne le score de la query en paramètre
        la métrique de score utilisée est le scorer (RR/Precision/Recall/...)
        """
        self.ranking = self.model.getRanking(query.txt)
        liste = [i for (i,s) in self.ranking]
        return scorer.evalQuery(liste, query)

    def evaluateQueries(self, queries, scorer):
        """
        retourne la moyenne des scores de chaque query de la liste.
        le score est obtenu d'après evaluateQuery

        le paramètre queries est un QueryParser
        """
        res = [self.evaluateQuery(query, scorer) for query in queries.collectionQuery.values()]
        return np.mean(res), np.std(res)

    def evaluateQueriesFromDict(self, collection, scorer):
        """
        le paramètre collection est un dictionnaire de {id_query:Query}
        """
        res = [self.evaluateQuery(query, scorer) for query in collection.values()]
        return np.mean(res), np.std(res)
