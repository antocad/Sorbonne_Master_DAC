#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

class Query:
    def __init__(self, identifiant, txt, liste_id, liste_rel):
        self.identifiant = identifiant
        self.txt = txt
        self.liste_id = liste_id
        self.liste_rel = liste_rel

class QueryParser:
    def __init__(self, qry, rel):
        self.collectionQuery = dict()
        txt = self.buildQueryCollectionRegex(qry)
        listePertinence = self.getListePertinence(rel)

        for identifiant,text in txt.items():
            if identifiant not in listePertinence:
                self.collectionQuery[identifiant] = Query(identifiant, text, [], [])
            else:
                #comme nous n'avons pas les notes de pertinences, nous les mettons toutes à 1
                liste_rel = [1]*len(listePertinence[identifiant])
                self.collectionQuery[identifiant] = Query(identifiant, text, listePertinence[identifiant], liste_rel)

    def buildQueryCollectionRegex(self, fichier):
        f = open(fichier, "r")
        tab = re.findall(r"\.I (\d+)\n(.W([^\.]*))?",
               f.read(),
               re.DOTALL)
        return {int(tab[i][0]): re.sub(r"^[\n ]*","",tab[i][2].replace('\n',' '))[:-1]for i in range(len(tab)) }

    def getListePertinence(self, fichier):
        res = dict()
        f = open(fichier, "r")
        ligne = f.readline()
        while ligne:
            tab = re.split(r"\s", ligne)
            tab = list(filter(('').__ne__, tab))
            if int(tab[0]) not in res:
                res[int(tab[0])] = [int(tab[1])]
            else:
                res[int(tab[0])].append(int(tab[1]))
            ligne = f.readline()
        return res
