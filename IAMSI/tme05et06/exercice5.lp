{maison(1..5, 1..5, 1..5, 1..5, 1..5, 1..5)}.
%maison(position, couleur, personne_de_nationalité, animal, marque_de_cigarettes, boisson)
%COULEURS
% 1 rouge
% 2 vert
% 3 blanc
% 4 jaune
% 5 bleue
%PERSONNES DE NATIONALITE
% 1 britannique
% 2 suedois
% 3 danois
% 4 norvegien
% 5 allemand
%ANIMAL
% 1 chien
% 2 oiseaux
% 3 chat
% 4 chevaux
% 5 poisson
%MARQUE DE CIGARETTES
% 1 pall mall
% 2 dunhill
% 3 blend
% 4 bluemaster
% 5 princess
%BOISSONS
% 1 thé
% 2 café
% 3 lait
% 4 bière
% 5 eau

% contraintes d'unicité sur les maisons
:- 6{maison(_,_,_,_,_,_)}.
:- {maison(_,_,_,_,_,_)}4.
:- maison(P,C1,_,_,_,_), maison(P,C2,_,_,_,_), C1<C2.
:- maison(_,C,P1,_,_,_), maison(_,C,P2,_,_,_), P1<P2.
:- maison(_,_,P,A1,_,_), maison(_,_,P,A2,_,_), A1<A2.
:- maison(_,_,_,A,M1,_), maison(_,_,_,A,M2,_), M1<M2.
:- maison(_,_,_,_,M,B1), maison(_,_,_,_,M,B2), B1<B2.
:- maison(P1,_,_,_,_,B), maison(P2,_,_,_,_,B), P1<P2.

%contraintes du sujet
:- not maison(_,1,1,_,_,_). %1
:- not maison(_,_,2,1,_,_). %2
:- not maison(_,_,3,_,_,1). %3
:- maison(P1,2,_,_,_,_), maison(P2,3,_,_,_,_), P1>=P2. %4
:- not maison(_,2,_,_,_,2). %5
:- not maison(_,_,_,2,1,_). %6
:- not maison(_,4,_,_,2,_). %7
:- not maison(3,_,_,_,_,3). %8
:- not maison(1,_,4,_,_,_). %9
% 10
:- maison(P1,_,_,_,3,_), maison(P2,_,_,3,_,_), P1-P2>1.
:- maison(P1,_,_,_,3,_), maison(P2,_,_,3,_,_), P1-P2<-1.
:- maison(P1,_,_,_,3,_), maison(P2,_,_,3,_,_), P1-P2==0.
% 11
:- maison(P1,_,_,_,2,_), maison(P2,_,_,4,_,_), P1-P2>1.
:- maison(P1,_,_,_,2,_), maison(P2,_,_,4,_,_), P1-P2<-1.
:- maison(P1,_,_,_,2,_), maison(P2,_,_,4,_,_), P1-P2==0.
:- not maison(_,_,_,_,4,4). %12
:- not maison(_,_,5,_,5,_). %13
%14
:- maison(P1,5,_,_,_,_), maison(P2,_,4,_,_,_), P1-P2>1.
:- maison(P1,5,_,_,_,_), maison(P2,_,4,_,_,_), P1-P2<-1.
:- maison(P1,5,_,_,_,_), maison(P2,_,4,_,_,_), P1-P2==0.
%15
:- maison(P1,_,_,_,3,_), maison(P2,_,_,_,_,5), P1-P2>1.
:- maison(P1,_,_,_,3,_), maison(P2,_,_,_,_,5), P1-P2<-1.
:- maison(P1,_,_,_,3,_), maison(P2,_,_,_,_,5), P1-P2==0.

possedePoisson(X) :- maison(_,_,X,5,_,_).

%ceux qui peuvent posseder des poissons sont: (il y a 7 solutions possibles en tout)
% danois, norvegien ou allemand


