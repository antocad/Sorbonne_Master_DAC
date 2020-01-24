# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import pulp
#import projet as proj

def stratOpti(G,D):
    nbVar = D + 1
    nbCont = D + 1

    a = np.zeros((nbCont,nbVar))
    a[0:D,1:D+1]=np.transpose(G)
    
    #le Z passer de l'autre coté
    a[:,0]=-1
    
    #la somme des proba = 1
    a[-1,:]=1
    a[-1,0]=0 

    # Second membre
    b = [0]*D+[1]
    
    # Coefficients de la fonction objectif
    c = [1]+[0]*D
    
    my_lp_problem = pulp.LpProblem("Problem", pulp.LpMaximize)
    
    x=[pulp.LpVariable('z', lowBound=-1. , cat='Continuous')]#car esperance peut aller jusqu'à -1
    for i in range(1,nbVar):
        x.append(pulp.LpVariable('p%d'%(i), lowBound=0. , cat='Continuous'))
    
    #objectif function
    obj = pulp.LpAffineExpression()
    for j in  range(nbVar):
        obj += c[j] * x[j]
    my_lp_problem += obj ,"Z"
    
    #contraintes
    for i in range(nbCont):    
        cont = pulp.LpAffineExpression()
        for j in range(nbVar):
            cont += a[i,j]*x[j]
        if(i==nbCont-1):
            cont = cont == b[i]
        else:
            cont = cont >= b[i]
        my_lp_problem += cont
    #print(my_lp_problem)
    my_lp_problem.solve()
    
    if(pulp.LpStatus[my_lp_problem.status]!="Optimal"):#si pas de solution opti
        print('/!\\',pulp.LpStatus[my_lp_problem.status],'/!\\')
        print(my_lp_problem)
        assert False
    
    #for var in x[1:]:
     #   print var, var.varValue
    return np.array([var.varValue for var in x[1:]])

#####################################################################
###################### Fonction utile ###############################
#####################################################################
def Q(d,k):
    """
    Retourne le tableau des probas d'obtenir k points ou moins 
    en jetant d dès ou moins, sachant qu'aucun dès n'est tombé sur 1.
    """
    res=[ [0.0 for i in range(k+1)] for j in range(d+1) ]
    if(d>=1):
        for i in range(2,min(7,k+1)):#on traite les cas ou l'on aurait un index error
            res[1][i]=0.2

    for dtmp in range(2,d+1):
        for ktmp in range(2*dtmp, min((6*dtmp)+1,k+1) ):
            somme=0
            for j in range(2,7):
                if(ktmp-j>0):
                    somme+=res[dtmp-1][ktmp-j]
            res[dtmp][ktmp]= somme*0.2
    return res

def P(d,k):
    """
    Retourne le tableau des probas d'obtenir k points ou moins en jetant 
    d dès ou moins
    """
    res=Q(d,k)
    for i in range(1,d+1):
        const=(5/6)**i
        res[i][1]=1-const
        for j in range(2*i, min((6*i)+1,k+1) ):
            res[i][j]*=const

    return np.array(res)

def EP(d):
    """Retourne l'esperance en fonction de d"""
    return 4*d*(5/6)**d + 1 - (5/6)**d

def maximiserEsperance(D):
    """Retourne le nombre de dès d <= D qui maximise l'esperance de points"""
    espMax=EP(1)
    dmax=1
    for d in range(2,D+1):
        tmp=EP(d)
        if(espMax<tmp):
            espMax=tmp
            dmax=d
    return dmax

def coupOpti(D,N):
    """
    D : le nombre de des maxi
    N : le nombre de point à atteindre
    Retourne un tableau de N*N du nombre de des à lancer qui maximise
    l'esperance de gain du joueur 1 selon l'etat.
    """
    maxPointTour = 6*D#le maximum de point que l'on peut faire dans un tour
    tabP=P(D,maxPointTour)#on calcul le tableau P(nbPoint|nbdés)
    tabDrep = np.zeros((N,N))#le retour de la fonction

    #init de EG esperance de gain
    EG=np.zeros((N+6*D,N+6*D))
    EG[N:,:]=1
    EG[:N,N:]=-1

    #calcul pour chaque etat
    for j in range(N-1,-1,-1):
        for i in range(N-1,-1,-1):
            sommeMaxMin=-1#le max sur d1
            for d1 in range(1,D+1):
                sommeMin=1#le min sur d2
                for d2 in range(1,D+1):
                    #proba jointe P(k1,k2|d1,d2) donc la proba d'arriver 
                    #dans l'etat (i+k1,j+k2)
                    proba=tabP[d1,1:].reshape((maxPointTour,1))*tabP[d2,1:]
                    #somme des esperance des etats (i+k1,j+k2) fois leur proba d'être dans l'etat
                    tmp=proba*EG[i+1:i+1+maxPointTour,j+1:j+1+maxPointTour]
                    somme=tmp.sum()
                    #recup le min
                    sommeMin=min(sommeMin,somme)
                #on recup le max et le nombre de dés que le j1 a lancé pour l'obtenir 
                if(sommeMaxMin<sommeMin):
                    drep=d1
                    sommeMaxMin=sommeMin
            
            #on met à jour les 2 tableau 
            EG[i,j]=sommeMaxMin
            tabDrep[i,j]=drep
            
    return tabDrep, EG

def gainExp(nbParties,jeu):
    """
    Calcul du gain experimentalement pour le joueur 1
    """
    score=[0,0]
    for n in range(nbParties):
        jeu.clear()
        g=jeu.jouerPartie()
        if(g!=0):#partie nulle, n'a d'interet que pour la variante simultanée
            score[g-1]+=1

    return (score[0]-score[1])/(nbParties)

def EG1_1coup(d1,d2,D):
    """
    Renvoie l'esperance de gain du joueur 1 pour le jeu en un coup
    """
    p=P(max(d1,d2),6*D)
    pWin=0
    for k1 in range(1,(6*d1)+1):
        for k2 in range(1,k1):
            pWin+= (p[d1,k1]*p[d2,k2])#proba de win
    pLose=0
    for k2 in range(1,(6*d2)+1):
        for k1 in range(1,k2):
            pLose+= (p[d1,k1]*p[d2,k2])#proba de lose
    return pWin-pLose#esperance

def Gain_1coup(D):
    """
    Renvoie la matrice D*D des gains (donc l'indice est décaler de -1)
    pour le jeu en un coup
    """
    res = np.zeros((D,D))
    for d1 in range(1,D+1):
        for d2 in range(1,D+1):
            res[d1-1][d2-1]=EG1_1coup(d1,d2,D)
    return res

def E1(p1,p2,EG1,D,tabP=[]):
    """
    p1 : nombre de point du joueur 1
    p2 : nombre de point du joueur 2
    EG1 : la matrice de l'esperance de gain du joueur 1
    D : le nombre de dés max
    renvoie la matrice E1 D*D representant l'esperance de gain du joueur 1 selon
    le nombre de dés qu'il a lancer et que son adversaire a lancé.
    (l'indice est décaler de -1)
    """
    maxPointTour = 6*D#le maximum de point que l'on peut faire dans un tour
    if len(tabP)==0:
        tabP=P(D,maxPointTour)#on calcul le tableau P(D,maxPointTour)
    res=np.zeros((D,D))

    for d1 in range(1,D+1):
        for d2 in range(1,D+1):
            proba=tabP[d1,1:].reshape((maxPointTour,1))*tabP[d2,1:]
            tmp=proba*EG1[p1+1:p1+maxPointTour+1,p2+1:p2+maxPointTour+1]
            res[d1-1,d2-1]=tmp.sum()

    return res

def EG1_Simultane(D,N):
    maxPointTour = 6*D
    #init de E
    EG=np.zeros((N+6*D,N+6*D))
    for i in range(0,N+6*D):
        for j in range(0,N+6*D):
            if(i<N and j<N):
                continue
            if(i>j):
                EG[i,j]=1.
            if(j>i):
                EG[i,j]=-1.
    EG[:N,:N]=np.NaN
                
    tabP=P(D,6*D)
    
    tabStrat=np.array([[None for i in range(N)] for j in range(N)])
    
    for i in range(N-1,-1,-1):
        for j in range(N-1,i-1,-1):
            Ej1 = E1(i,j,EG,D,tabP)#gain
            vp1 = np.array(stratOpti(Ej1,D))#distrib de proba du j1
            
            Ej2 = E1(j,i,EG,D,tabP)
            vp2 = np.array(stratOpti(Ej2,D))#calcul strat de j2 en le plaçant comme le j1 en inversent les scores
        
            tmp = ((tabP[1:,1:]*vp1.reshape((D,1))).sum(0))
            tmp = tmp.reshape((6*D,1))*((tabP[1:,1:]*vp2.reshape((D,1))).sum(0))
            tmp = tmp*EG[i+1:i+maxPointTour+1,j+1:j+maxPointTour+1]
            
            EG[i,j] = tmp.sum()
            EG[j,i] = -EG[i,j]
            
            tabStrat[i,j]=vp1
            tabStrat[j,i]=vp2
            
    return tabStrat,EG[:N+1,:N+1]
            
#####################################################################
###################### Classe joueur et jeu #########################
#####################################################################
    
################ joueur variante séquentielle #######################
class JoueurAveugle:
    """Joue tout le temps le nombre de dés qui maximise son esperance de points"""
    def __init__(self,D,N):
        self.d = maximiserEsperance(D)

    def joue(self,p1,p2):
        return self.d    

class JoueurOpti:
    """Joue le plus optimalement selon le score des joueurs"""
    def __init__(self,D,N):
        self.strat, self.esp = coupOpti(D,N)

    def joue(self,p1,p2):
        return self.strat[p1,p2]
    
class JoueurRandom:
    """Joue un nombre de dés aléatoire"""
    def __init__(self,D,N):
        self.d = D

    def joue(self,p1,p2):
        return np.random.randint(self.d)+1
    
class JoueurBorne:
    """Joue tout le temps le nombre de dés d passer en paramètre"""
    def __init__(self,D,N,d=1):
        self.d = d

    def joue(self,p1,p2):
        return self.d

################ joueur variante jeu en un coup #####################
class JoueurOptiSimple():
    def __init__(self,D):
        self.strat=np.array(stratOpti(Gain_1coup(D),D))

    def joue(self):
        return np.argmax(self.strat.cumsum()>np.random.rand())+1

class JoueurAveugleSimple():
    def __init__(self,D):
        self.d = maximiserEsperance(D)

    def joue(self):
        return self.d
    
################ joueur variante simultanée #######################
class JoueurOptiSimultane:
    def __init__(self,D,N):
        self.strat,_ = EG1_Simultane(D,N) 

    def joue(self,p1,p2):
        return np.argmax(self.strat[p1,p2].cumsum()>np.random.rand())+1


    
class JoueurHumain:
    def __init__(self,D,N):
        self.d = D
########################## Jeux ####################################
class Jeu:
    def __init__(self,J1,J2,D,N):
        self.j1=J1
        self.j2=J2
        self.D=D
        self.N=N
        self.p1=0
        self.p2=0

    def echangerJoueur(self):
        tmp=self.j2
        self.j2=self.j1
        self.j1=tmp

    def clear(self):
        self.p1=0
        self.p2=0

    def lancerDes(self,n):
        score=0
        for i in range(int(n)):
            val = np.random.randint(6)+1
            if(val==1):
                return 1
            score+=val
        return score

    def jouerPartie(self):
        while(self.p1<self.N and self.p2<self.N):
            n=self.j1.joue(self.p1,self.p2)
            self.p1+=self.lancerDes(n)
            if(self.p1>=self.N):
                return 1
            n=self.j2.joue(self.p2,self.p1)
            self.p2+=self.lancerDes(n)
            if(self.p2>=self.N):
                return 2

    def jouerCoup(self, n=0):
        #le cas où le joueur 1 joue (lorsque le dé en paramètre est >0
        if(n>0):
            val = self.lancerDes(n)
            self.p1+=val
            return (n,val,[self.p1,self.p2])
        #le cas où le joueur 2 joue (par défaut)
        n=self.j2.joue(self.p1,self.p2)
        val = self.lancerDes(n)
        self.p2+=val
        return (n,val,[self.p1,self.p2])

class JeuSimple(Jeu):
    """jeu en 1 coup"""
    def __init__(self,J1,J2,D):
        self.j1=J1
        self.j2=J2
        self.D=D
        self.p1=0
        self.p2=0
        
    def jouerPartie(self):
        d1=self.j1.joue()
        d2=self.j2.joue()
        self.p1=self.lancerDes(d1)
        self.p2=self.lancerDes(d2)
        #print(d1,d2,self.p1,self.p2)
        if(self.p1>self.p2):
            return 1
        elif(self.p2>self.p1):
            return 2
        else:
            return 0
        
class JeuSimultane(Jeu):
    def jouerPartie(self):
        while(self.p1<self.N and self.p2<self.N):
            tmp=self.lancerDes(self.j1.joue(self.p1,self.p2))
            self.p2+=self.lancerDes(self.j2.joue(self.p2,self.p1))
            self.p1+=tmp
        if(self.p1>self.p2):
            return 1
        if(self.p2>self.p1):
            return 2
        else: 
            return 0

#####################################################################
###################### Interface ####################################
#####################################################################
def printHeader():
    print("""
      _ _             _           _   _   _
     | (_)           | |         | | | | | |
   __| |_  ___ ___   | |__   __ _| |_| |_| | ___
  / _` | |/ __/ _ \  | '_ \ / _` | __| __| |/ _ \\
 | (_| | | (_|  __/  | |_) | (_| | |_| |_| |  __/
  \__,_|_|\___\___|  |_.__/ \__,_|\__|\__|_|\___|

    """)

def printStats(N,D,s1,s2):
    print "----- Scores:\nJoueur1:",s1," |  Joueur2:",s2
    print("#################################################")

def main():
    printHeader()

    N = int(input("Nombre de points pour gagner:"))
    D = int(input("Nombre de dés maximum:"))

    j1 = JoueurHumain(D,N)

    j2 = int(input("Stratégie de l'adversaire?\n1:Aléatoire\n2:Aveugle\n3:Optimale (Il faut attendre le chargement)\n"))
    if j2==1:
        j2=JoueurRandom(D,N)
    elif j2==2:
        j2=JoueurAveugle(D,N)
    else:
        j2=JoueurOpti(D,N)

    partie = Jeu(j1,j2,D,N)
    printStats(N,D,partie.p1,partie.p2)

    while (partie.p1 < N and partie.p2 < N):
        print("----- Votre tour -----")
        nbDe = 0
        while nbDe < 1 or nbDe > D:
            nbDe = int(input("Combien de dés lancer? "))
        (n,v,s) = partie.jouerCoup(nbDe)
        print "Score obtenu:",v
        if (s[0]<N):
            print "----- Tour de l'Adversaire -----"
            (n,v,s) = partie.jouerCoup()
            print "Nombre de dés lancés:",int(n)
            print "Score obtenu:",v
        printStats(N,D,partie.p1,partie.p2)
    if (partie.p1>=N):
        print("Joueur 1 a gagné")
    else:
        print("Joueur 2 a gagné")

main()