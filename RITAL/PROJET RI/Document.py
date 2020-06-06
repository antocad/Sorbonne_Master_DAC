#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:36:09 2020

@author: 3670631
"""
import re

class Document():
    def __init__(self, I, contenu):
        self.contenu = contenu
        self.I = I
        self.T = re.findall(r"^\.T\n([^µ]*?)\n\.", contenu, re.MULTILINE)
        if (len(self.T)>0):
            self.T = self.T[0]
        else:
            self.T = ""
        self.B = re.findall(r"^\.B\n([^µ]*?)\n\.", contenu, re.MULTILINE)
        self.A = re.findall(r"^\.A\n([^µ]*?)\n\.", contenu, re.MULTILINE)
        self.K = re.findall(r"^\.K\n([^µ]*?)\n\.", contenu, re.MULTILINE)
        self.W = re.findall(r"^\.W\n([^µ]*?)\n\.", contenu, re.MULTILINE)
        if (len(self.W)>0):
            self.W = self.W[0]
        else:
            self.W = ""
        self.X = re.findall(r"\.X\n([^µ]*?)\n\.", contenu, re.MULTILINE)
        self.text = self.T+" "+self.W #normalement self.W d'après le sujet du tme1
        self.identifiant = self.I #redondant, mais par soucis de version

    def getNbMot(self):
        return len(self.text.split())

    def show(self):
        print(self.I, '\nT: ',self.T, '\nB: ',self.B,'\nA: ',self.A,'\nK: ',
              self.K, '\nW: ',self.W, '\nX: ',self.X)
