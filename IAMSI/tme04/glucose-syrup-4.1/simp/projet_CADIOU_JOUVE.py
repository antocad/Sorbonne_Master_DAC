# -*- coding: utf-8 -*-

# PROJET IAMSI 2019-2020
#
# Vincent JOUVE 3671083
# Antoine CADIOU 3670631
#
# IMPORTANT : Pour fonctionner, ce script doit être dans le même dossier que le script de glucose_static
# Il existe 3 façons de lancer le script.
# Les options de lancement du script pour chacune d'entre elles sont:
#
# 1)
#   - le nom du fichier avec les noms des équipes (qui se trouve dans le même dossier que ce script python)
#   - Le nombre d'équipes
#   - le nombre de jours
#
# 2) (le script va chercher le nombre de jours minimal pour que la compétition soit réalisable avec les contraintes)
#   - Le nombre d'équipes
#
# 3) Aucun argument: le script va regarder pour un nombre d'équipes variant de 3 à 10 le nombre de jours minimal pour que la compétition puisse être organisée

import os
import sys

in_file = "tmp_in.cnf"
out_file = "tmp_out.cnf"

def nbVar(ne,nj):
    return (nj-1)*ne*ne+(ne-1)*ne+(ne-1)+1

def codage(ne,nj,j,x,y):
    return (j*(ne**2))+(x*ne)+y+1

def decodage(ne,nj,k):
    y = (k-1) % ne
    x = (k-y-1)%(ne**2)/ne
    j = (k-1-x*ne-y)/(ne**2)
    return j,x,y

def clauseAuMoins(l):
    return ' '.join(map(str,l)) + ' 0'

def clauseAuPlus(l):
    tmp = ''
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            tmp += str(-l[i])+' '+str(-l[j])+' 0\n'
    return tmp[:-1]

def encoderC1(ne, nj):
    res = ''
    for j in range(nj):
        for e1 in range(ne):
            l = []
            for e2 in range(ne):
                if e1!=e2:
                    v1 = codage(ne,nj,j,e1,e2)
                    v2 = codage(ne,nj,j,e2,e1)
                    l.append(v1)
                    l.append(v2)
            if l != []:
                res += clauseAuPlus(l)+'\n'
    return res[:-1]

def encoderC2(ne, nj):
    res = ''
    for e1 in range(ne):
        for e2 in range(ne):
            if (e1 !=e2 ):
                aller = []
                retour = []
                for j in range(nj):
                    allerVal = codage(ne,nj,j,e1,e2)
                    retourVal = codage(ne,nj,j,e2,e1)
                    aller.append(allerVal)
                    retour.append(retourVal)
                if aller != [] and retour != []:
                    res += clauseAuPlus(aller)+'\n'
                    res += clauseAuPlus(retour)+'\n'
                    res += clauseAuMoins(aller)+'\n'
                    res += clauseAuMoins(retour)+'\n'
    return res[:-1]

def encoder(ne, nj):
    """encode toutes les contraintes pour faire un planning"""
    #contrainte sup les equipes ne peuvent pas s'affronter elles-meme
    contrainte = ''
    for e in range(ne):
        for j in range(nj):
            contrainte += str(-codage(ne,nj,j,e,e))+' 0\n'
    return contrainte+encoderC1(ne, nj) +'\n'+ encoderC2(ne, nj)+'\n'+ \
                contrainteExtDimanche(ne,nj,0.5)+'\n'+contrainteDomDimanche(ne,nj,0.4)+'\n'+ \
                contrainteExtConsecutif(ne,nj)+'\n'+contrainteDomConsecutif(ne,nj)

def createCNF(nom, ne, nj):
    """créer un fichier de config"""
    contraintes = encoder(ne, nj)
    with open(nom, "w") as f:
        f.write("p cnf " + str(nbVar(ne, nj)) + " " + str(len(contraintes.split('\n'))) + "\n"+contraintes)
    #print("file "+nom+" created.")

def decoder(fichier, ne, nj):
    """decode la sortie du solveur renvoie une liste
    de triplet jour, eq1, eq2 d'un model
    """
    with open(fichier, "r") as f:
        line = f.read()
    if(line.startswith('UNSAT')):
        return -1
    if(len(line)==0):#inconnu
        return -2
    line = line.split(' ')[:-1]
    line = [decodage(ne, nj, int(i)) for i in line if int(i) > 0]
    return line

def planning(equipes, ne, nj):
    line = execute(ne,nj)
    line = decoder(out_file, ne, nj)
    if(line == -1):
        print('impossible')
        return
    if(line == -2):
        print('inconnu')
        return
    for (j,e1,e2) in line:
        print("jour:",int(j),equipes[int(e1)],"vs",equipes[int(e2)])

def execute(ne,nj):
    createCNF(in_file, ne, nj)
    return os.system("timeout 10s ./glucose_static "+in_file+" "+out_file+" > /dev/null")

def nbJourMin(ne):
    """renvoie nb jour minimal pour ne equipe"""
    d=1
    f=10
    #on trouve un f qui marche
    execute(ne,f)
    line = decoder(out_file,ne,f)
    while(line == -1 or line==-2):
        f=2*f
        execute(ne,f)
        line = decoder(out_file,ne,f)
    #dichotomie
    while(d<f):
        m=(f+d)//2
        execute(ne,m)
        line = decoder(out_file,ne,m)
        if(line == -1 or line==-2):
            d=m+1
        else:
            f=m
    return f

def kparmi(liste,k):
    res =[]
    if (len(liste)<k):
        return []
    if (k==0):
        return []
    if (k==1):
        return [str(-e) for e in liste]
    for i in range(len(liste)):
        res += [str(-liste[i])+' '+str(e) for e in kparmi(liste[i+1:],k-1)]
    return res

def clauseAuPlusK(liste,k):
    return '\n'.join([e+' 0' for e in kparmi(liste,k+1)])

def clauseAuMoinsK(liste,k):
    return '\n'.join([e+' 0' for e in kparmi([-e for e in liste],len(liste)-k+1)])

def contrainteExtDimanche(ne,nj,pext):
    """pext% des match à l'exterieur sont les dimanches"""
    res = ''
    nbmatch = int(((ne-1)*pext)+1)
    for e1 in range(ne):
        l = []
        for j in range(1,nj,2):#les dimanches -> jours impairs
            for e2 in range(ne):
                if(e1!=e2):
                    l.append(codage(ne,nj,j,e2,e1))
        tmp = clauseAuMoinsK(l,nbmatch)
        if(len(tmp)==0):
            print(l,nbmatch)
        res += clauseAuMoinsK(l,nbmatch)+'\n'
    return res[:-1]

def contrainteDomDimanche(ne,nj,pdom):
    """pdom% des match à domicile sont les dimanches"""
    res = ''
    nbmatch = int(((ne-1)*pdom)+1)
    for e1 in range(ne):
        l = []
        for j in range(1,nj,2):#les dimanches -> jours impairs
            for e2 in range(ne):
                if(e1!=e2):
                    l.append(codage(ne,nj,j,e1,e2))
        tmp = clauseAuMoinsK(l,nbmatch)
        if(len(tmp)==0):
            print(l,nbmatch)
        res += clauseAuMoinsK(l,nbmatch)+'\n'
    return res[:-1]

def contrainteExtConsecutif(ne,nj):
    res=''
    for e1 in range(ne):
        for j in range(nj-2):
            l = []
            for e2 in range(ne):
                if(e1!=e2):
                    for i in range(3):
                        l.append(codage(ne,nj,j+i,e2,e1))
        res += clauseAuPlusK(l,2)+'\n'
    return res[:-1]

def contrainteDomConsecutif(ne,nj):
    res=''
    for e1 in range(ne):
        for j in range(nj-2):
            l = []
            for e2 in range(ne):
                if(e1!=e2):
                    for i in range(3):
                        l.append(codage(ne,nj,j+i,e1,e2))
        res += clauseAuPlusK(l,2)+'\n'
    return res[:-1]

def fichierEquipeToDict(path):
    with open(path,'r') as f:
        return dict(enumerate(f.read().split('\n')))


if __name__=='__main__':
    args = sys.argv

    if(len(args) == 4 ) :
        pathEquipes = args[1]
        ne = int(args[2])
        nj = int(args[3])
        equipes = fichierEquipeToDict(pathEquipes)
        planning(equipes, ne, nj)
    elif(len(args) == 2):
        ne = int(args[1])
        print(nbJourMin(ne))
    else:
        for ne in range(3,11):
            print("Pour",ne,"equipes il faut",nbJourMin(ne),"au minimum pour organiser un tournoi")
