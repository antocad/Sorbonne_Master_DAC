#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:42:33 2019

@author: 3670631
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:28:20 2019

@author: 3670631
"""

#!/usr/bin/python

# Copyright 2013, Gurobi Optimization, Inc.


from gurobipy import *



nbcont=3
nbvar=2

# Range of plants and warehouses
lignes = range(nbcont)
colonnes = range(nbvar)

# Matrice des contraintes
a = [[1,3],
     [2,1],
     [3,1]]

# Second membre
b = [7,3,5]

# Coefficients de la fonction objectif
c = [8,5]

m = Model("mogplex")     
        
# declaration variables de decision
x = []
for i in colonnes:
    x.append(m.addVar(vtype=GRB.INTEGER, lb=0, name="x%d" % (i+1)))

# maj du modele pour integrer les nouvelles variables
m.update()

obj = LinExpr();
obj =0
for j in colonnes:
    obj += c[j] * x[j]
        
# definition de l'objectif
m.setObjective(obj,GRB.MAXIMIZE)

# Definition des contraintes
for i in lignes:
    m.addConstr(quicksum(a[i][j]*x[j] for j in colonnes) <= b[i], "Contrainte%d" % i)

# Resolution
m.optimize()


print("")                
print('Solution optimale:')
for j in colonnes:
    print('x%d'%(j+1), '=', x[j].x)
print("")
print('Valeur de la fonction objectif :', m.objVal)