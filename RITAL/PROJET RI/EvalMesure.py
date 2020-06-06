#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

class EvalMesure:
    def evalQuery(self, liste, query):
        raise NotImplementedError()

class Precision(EvalMesure):
    """
    evalQuery retourne la précision du modèle sur la requête.
    """
    def __init__(self, k):
        self.k = k

    def evalQuery(self, liste, query):
        score = 0
        for i in range(self.k):
            if liste[i] in query.liste_id:
                score += 1
        return score/self.k

class Recall(EvalMesure):
    """
    evalQuery retourne la valeur de rappel du modèle sur la requête.
    """
    def __init__(self, k):
        self.k = k

    def evalQuery(self, liste, query):
        score = 0
        if len(query.liste_id) == 0:
            return 1
        for i in range(self.k):
            if liste[i] in query.liste_id:
                score += 1
        return score/len(query.liste_id)

class Fmeasure(EvalMesure):
    """
    evalQuery retourne la Fmeasure du modèle sur la requête.
    par défaut beta=1, donc on calcule la F1-mesure
    """
    def __init__(self, k, beta=1):
        self.k = k
        self.beta = beta

    def evalQuery(self, liste, query):
        p = Precision(self.k).evalQuery(liste, query)
        r = Recall(self.k).evalQuery(liste, query)
        if p==0 and r==0:
            return 0
        return (1+self.beta**2)*(p*r)/(self.beta**2*(p+r))

class AvgP(EvalMesure):
    """
    evalQuery retourne la précision moyenne du modèle sur la requête.

    Lorsqu'on fait la moyenne de cette métrique sur plusieurs requetes, on obtiens le score MAP
    """
    def evalQuery(self, liste, query):
        if len(query.liste_id) == 0:
            return 0
        somme = 0
        for k in range(len(liste)):
            p = Precision(k+1).evalQuery(liste, query)
            if liste[k] in query.liste_id:
                somme += p
        return somme/len(query.liste_id)

class RR(EvalMesure):
    """
    evalQuery retourne le réciprocal rank du modèle sur la requête,
    c'est à dire 1/rang du premier resultat pertinent retourné.

    Lorsqu'on fait la moyenne de cette métrique sur plusieurs requetes, on obtiens le score MRR
    """
    def evalQuery(self, liste, query):
        for i in range(len(liste)):
            if liste[i] in query.liste_id:
                return 1/(i+1)
        return 0

class NDCG(EvalMesure):
    """
    evalQuery retourne le score NDCG du modèle sur la requête,

    Etant donné que la liste des pertinences n'est pas ordonnée, on les a supposées toutes égales à 1,
    donc ici avec nos données ce n'est pas intéressant d'étudier ce score.
    Cependant il est fonctionnel est pourrait être utilisé si on disposait des données adéquates.
    """
    def __init__(self, p):
        self.p = p

    def evalQuery(self, liste, query):
        if len(query.liste_id) == 0:
            return 1
        dcg = 0
        for i in range(self.p):
            if liste[i] in query.liste_id:
                if i==0:
                    num = 1
                else:
                    num = math.log2(i+1)
                dcg += query.liste_rel[\
                         query.liste_id.index(liste[i])]/num
        liste_idcg = np.argsort(query.liste_rel)[::-1]
        idcg = query.liste_rel[liste_idcg[0]]
        for i in range(1, len(liste_idcg)):
            idcg += query.liste_rel[liste_idcg[i]] / math.log2(i+1)
        return dcg/idcg
