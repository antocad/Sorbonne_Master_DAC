#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:36:41 2020

@author: 3670631
"""
from Document import Document
import re

class Parser():
    def __init__(self, fileURI):
        self.collection = dict()
        tab = separateCorpus(fileURI)
        for I,doc in tab:
            self.collection[I] = Document(I, doc)
            
def buildDocumentCollectionRegex(fichier):
    f = open(fichier, "r")
    tab = re.findall(r"\.I (\d+)\n(.T([^\.]*))?",
           f.read(),
           re.DOTALL)
    return [(int(tab[i][0]), re.sub(r"^[\n ]*","",tab[i][2].replace('\n',' '))[:-1])\
           for i in range(len(tab))]

def buildDocCollectionSimple(fichier):
    balises=[".B",".A",".N",".X",".K",".W"]
    f = open(fichier, "r")
    tab = []
    check = False
    line = f.readline()
    while(line):
        decoupe = line.split(".I ")
        if len(decoupe)>1:
            tab.append([decoupe[-1],""])
            check = False
        else:
            if not check and line[0:2]==".T" :
                check = True
                tab[-1][1] += line[3:]
            elif check and line[0:2] not in balises:
                tab[-1][1] += line
            if line[0:2] in balises:
                check = False
        line = f.readline()
    return [(int(tab[i][0]),re.sub(r"^[\n ]*","",tab[i][1].replace('\n',' '))[:-1])\
            for i in range(len(tab))]

def separateCorpus(fichier):
    f = open(fichier, "r")
    tab = []
    line = f.readline()
    while(line):
        if re.match(r"^.*\.I \d*\n$", line):
            tab.append([int(re.findall(r"^.*\.I (\d*)\n$", line)[0]),""])
        else:
            tab[-1][1] += line
        line = f.readline()
    return tab