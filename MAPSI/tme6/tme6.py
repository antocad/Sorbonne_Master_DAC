#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:06:30 2019

Antoine Cadiou: 3670631
Vincent Jouve: 3671083
"""

import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt

with open('ressources/lettres.pkl', 'rb') as f:
    data = pkl.load(f, encoding='latin1') 
X = np.array(data.get('letters')) # récupération des données sur les lettres
Y = np.array(data.get('labels')) # récupération des étiquettes associées 


# affichage d'une lettre
def tracerLettre(let):
    a = -let*np.pi/180; # conversion en rad
    coord = np.array([[0, 0]]); # point initial
    for i in range(len(a)):
        x = np.array([[1, 0]]);
        rot = np.array([[np.cos(a[i]), -np.sin(a[i])],[ np.sin(a[i]),np.cos(a[i])]])
        xr = x.dot(rot) # application de la rotation
        coord = np.vstack((coord,xr+coord[-1,:]))
    plt.figure()
    plt.plot(coord[:,0],coord[:,1])
    plt.savefig("exlettre.png")
    return

def discretise(x, d):
    intervalle = 360 / d
    return np.floor(x / intervalle)

def groupByLabel(y):
    index = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y == i)
        index.append(ind)
    return index

def learnMarkovModel(Xc, d):
    A = np.ones((d, d))
    Pi = np.ones(d)
    for x in Xc:
        Pi[int(x[0])]+=1
        for i in range(1,len(x)):
            A[int(x[i-1]),int(x[i])]+=1
            
    A = A / np.maximum(A.sum(1).reshape(d, 1), 1) # normalisation
    Pi = Pi / Pi.sum()
    return Pi, A

def probaSequence(s, Pi, A):
    res = np.log(Pi[int(s[0])])
    for i in range(1, len(s)):
        res += np.log(A[int(s[i-1]),int(s[i])])
    return res

# separation app/test, pc=ratio de points en apprentissage
def separeTrainTest(y, pc):
    indTrain = []
    indTest = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y == i)
        n = len(ind)
        indTrain.append(ind[np.random.permutation(n)][:int(np.floor(pc * n))])
        indTest.append(np.setdiff1d(ind, indTrain[-1]))
    return indTrain, indTest

# exemple d'utilisation
itrain, itest = separeTrainTest(Y, 0.8)
ia = []
for i in itrain:
    ia += i.tolist()    
it = []
for i in itest:
    it += i.tolist()


d = 20        # paramètre de discrétisation
Xd = np.array([discretise(x, d) for x in X[ia]])   # application de la discrétisation
index = groupByLabel(Y[ia])  # groupement des signaux par classe
models = []
for cl in range(len(np.unique(Y[ia]))): # parcours de toutes les classes et optimisation des modèles
    models.append(learnMarkovModel(Xd[index[cl]], d))
    
proba = np.array([[probaSequence(discretise(x,d), models[cl][0], models[cl][1]) for x in X[it] ]
                  for cl in range(len(np.unique(Y[it])))])
# calcul d'une version numérique des Y :
Ynum = np.zeros(Y[it].shape)
for num, char in enumerate(np.unique(Y[it])):
    Ynum[Y[it] == char] = num
    
# Calcul de la classe la plus probable :
pred = proba.argmax(0) # max colonne par colonne

# Calcul d'un pourcentage de bonne classification :
perf=np.where(pred != Ynum, 0.,1.).mean()


confusion = np.zeros((26,26))
for label,prediction in zip(Ynum,pred):
    confusion[int(prediction)][int(label)] += 1

plt.figure()
plt.imshow(confusion, interpolation = 'nearest')
plt.colorbar()
plt.xticks(np.arange(26), np.unique(Y))
plt.yticks(np.arange(26), np.unique(Y))
plt.xlabel(u'Vérité terrain')
plt.ylabel(u'Prédiction')
plt.savefig("mat_conf_lettres.png")

def generate(Pi,A,n):
    res=[]
    p=np.random.rand()
    picum=Pi.cumsum()
    i=0
    while(picum[i]<p):
        i+=1
    res.append(i)
    for blabla in range(n):
        acum=A[res[-1],:].cumsum()
        p=np.random.rand()
        i=0
        while(acum[i]<p):
            i+=1
        res.append(i)
    return np.array(res)
    
newa = generate(models[0][0], models[0][1], 20)       # generation d'une séquence d'états
intervalle = 360. / d                                 # pour passer des états => valeur d'angles
newa_continu = np.array([i * intervalle for i in newa]) # conv int => double
tracerLettre(newa_continu)
