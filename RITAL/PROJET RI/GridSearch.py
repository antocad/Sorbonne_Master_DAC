#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import numpy as np
from EvalIRModel import *
from IRModel import *

def GridSearch(indexeur, queries, scorer, fromDict):
    """
    on procède par grid-search pour trouver le meilleur couple de paramètres b et k1 pour le modèle Okapi
    on peut facilement l'adapter pour trouver les paramètres optimaux d'un autre modèle (changer le double for + ligne 19)
    """
    liste_b = [b/100 for b in range(60, 95, 5)] #de 0.6 à 0.90(inclus) par pas de 0.05
    liste_k = [k/10 for k in range(10, 21)] #de 1 à 2(inclus) par pas de 0.1
    bestScore = 0
    bestCouple = None
    for b in liste_b:
        for k in liste_k:
            model = Okapi(indexeur, b, k)
            evalmodel = EvalIRModel(model)
            score = 0
            if fromDict:
                score = evalmodel.evaluateQueriesFromDict(queries, scorer)[0]
            else:
                score = evalmodel.evaluateQueries(queries, scorer)[0]
            if score > bestScore:
                bestScore = score
                bestCouple = (b, k)
    return bestScore, bestCouple

def cross_val(k, queries, indexeur, scorer):
    """
    cross_validation qui permet de renvoyer le score moyen sur k-folds après optimisation des paramètres b et k1 d'un modèle Okapi
    on peut facilement l'adapter pour trouver les paramètres optimaux d'un autre modèle (changer les lignes 58,59 et 60)
    """
    liste_queries = [q.identifiant for i,q in queries.collectionQuery.items()]
    random.shuffle(liste_queries)
    folds = []
    size = len(liste_queries)//k
    #création des k folds
    for i in range(k-1):
        folds.append(liste_queries[i*size:i*size+size])
    folds.append(liste_queries[(k-1)*size:])
    scores = []
    params = []
    #apprentissage sur k-1 et test sur le dernier
    for i in range(k):
        print("K =", i)
        train = folds[0:i] + folds[i+1:]
        train = np.hstack(train)
        test = folds[i]
        q_train = {indice:queries.collectionQuery[indice] for indice in train} 
        q_test = {indice:queries.collectionQuery[indice] for indice in test}
        #apprentissage des parametres sur le dictionnaire de train
        tmp, bestParams = GridSearch(indexeur, q_train, scorer, True)
        params.append(bestParams)
        #test du modèle avec les paramètres trouvés
        b = bestParams[0]
        k1 = bestParams[1]
        model = Okapi(indexeur, b, k1)
        evalmodel = EvalIRModel(model)
        scores.append(evalmodel.evaluateQueriesFromDict(q_test, scorer)[0])
    return scores,params