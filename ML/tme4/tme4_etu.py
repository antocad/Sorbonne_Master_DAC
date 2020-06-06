from arftools import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def mse(datax,datay,w):
    """ retourne la moyenne de l'erreur aux moindres carres """
    return np.mean((np.dot(datax, w.reshape((-1,1))) - datay)**2)

def mse_g(datax,datay,w):
    """ retourne le gradient moyen de l'erreur au moindres carres """
    return np.dot(2*datax.T, np.dot(datax, w.reshape(-1,1)) - datay)/len(datax)

def hinge(datax,datay,w):
    """ retourne la moyenne de l'erreur hinge """
    fx = np.dot(datax, w.reshape(-1,1))
    return np.mean(np.where(-datay*fx<0, 0, -datay*fx))

def hinge_g(datax,datay,w):
    """ retourne le gradient moyen de l'erreur hinge """
    tmp = datay * np.dot(datax, w.reshape(-1,1))
    n = len(datax)
    return np.dot(datax.T, np.where(tmp>0, 0, -datay))/n

def hinge_g2(datax,datay,w):
    """ retourne le gradient moyen de l'erreur hinge """
    tmp = datay*np.dot(datax, w.reshape(-1,1))
    t2 = -datay.reshape(-1,1)*datax    
    res = []
    for i in range(len(tmp)):
        if tmp[i]>0:
            res.append(np.zeros(len(w)))
        else:
            res.append(t2[i])
    return np.mean(np.array(res), axis=0)

def ridge(datax,datay,w,alpha):
    """ retourne le gradient de ridge """
    return mse(datax,datay,w) + alpha * np.sqrt(np.sum(w**2))**2

def ridge_g(datax,datay,w,alpha):
    """ retourne le gradient de ridge """
    return mse_g(datax,datay,w)+alpha * 2 * w.reshape((-1,1))

def lasso_g(datax,datay,w,alpha):
    """ retourne le gradient de lasso """
    return mse_g(datax,datay,w) + alpha * np.sign(w).reshape((-1,1))

class Lineaire(object):
    def __init__(self,loss=hinge,loss_g=hinge_g,max_iter=1000,eps=0.01):
        """ :loss: fonction de cout
            :loss_g: gradient de la fonction de cout
            :max_iter: nombre d'iterations
            :eps: pas de gradient
        """
        self.max_iter, self.eps = max_iter,eps
        self.loss, self.loss_g = loss, loss_g

    def fit(self,datax,datay,testx=None,testy=None, methode='batch'):
        """ :datax: donnees de train
            :datay: label de train
            :testx: donnees de test
            :testy: label de test
        """
        # on transforme datay en vecteur colonne
        datay = datay.reshape(-1,1)
        N = len(datay)
        datax = datax.reshape(N,-1)
        D = datax.shape[1]
        #self.w = 2*np.random.random((1,D)) - 1 #on tire entre -1 et 1
        self.w = np.zeros((1,D))
        for i in range(self.max_iter):
            if methode=='stochastic':
                indexrandom = np.random.randint(N,size=int(0.1*N))
                self.w = self.w - self.eps*self.loss_g(datax[indexrandom], datay[indexrandom], self.w).reshape(1,-1)
            elif methode=='minibatch':
                size = int(len(datax)*5/100)
                index = np.array(list(range(len(datax))))
                np.random.shuffle(index)
                self.w = self.w - self.eps * self.loss_g(datax[index[:size]], datay[index[:size]], self.w).reshape(1,-1)
            else:
                self.w = self.w - self.eps*self.loss_g(datax, datay, self.w).reshape(1,-1)
        
    def predict(self,datax):
        if len(datax.shape)==1:
            datax = datax.reshape(1,-1)
        return np.sign(np.dot(datax,self.w.reshape(-1,1))).reshape(1,-1)

    def score(self,datax,datay):
        pre = self.predict(datax)
        res = np.where(pre==datay,1,0)
        return np.mean(res)
        #return self.loss(datax,datay, self.w)


def load_usps(fn):
    with open(fn,"r") as f:
        f.readline()
        data = [[float(x) for x in l.split()] for l in f if len(l.split())>2]
    tmp=np.array(data)
    return tmp[:,1:],tmp[:,0].astype(int)

def show_usps(data):
    plt.imshow(data.reshape((16,16)),interpolation="nearest",cmap="gray")
    plt.colorbar()

def plot_error(datax,datay,f,step=10):
    grid,x1list,x2list=make_grid(xmin=-4,xmax=4,ymin=-4,ymax=4)
    plt.contourf(x1list, x2list, np.array([f(datax,datay,w) for w in grid]).reshape(x1list.shape), 25)
    plt.colorbar()
    plt.show()

if __name__=="__main__":
    """ Tracer des isocourbes de l'erreur """
    plt.ion()
    trainx,trainy =  gen_arti(nbex=1000,data_type=0,epsilon=1)
    testx,testy =  gen_arti(nbex=1000,data_type=0,epsilon=1)
    plt.figure()
    plot_error(trainx,trainy,mse)
    plt.figure()
    plot_error(trainx,trainy,hinge)
    perceptron = Lineaire(hinge,hinge_g,max_iter=1000,eps=0.1)
    perceptron.fit(trainx,trainy)
    print("Précision : train %f, test %f"% (perceptron.score(trainx,trainy),perceptron.score(testx,testy)))
    plt.figure()
    plot_frontiere(trainx,perceptron.predict,200)
    plot_data(trainx,trainy)
