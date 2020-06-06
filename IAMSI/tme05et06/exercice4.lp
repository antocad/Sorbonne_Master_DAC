nbNoeud(7).

noeud(1..Nb) :- nbNoeud(Nb).
n(1..Nb) :- nbNoeud(Nb).

arc(1,2).
arc(1,3).
arc(1,5).
arc(2,1).
arc(2,3).
arc(2,4).
arc(2,6).
arc(3,1).
arc(3,2).
arc(3,4).
arc(3,5).
arc(3,6).
arc(4,2).
arc(4,3).
arc(4,5).
arc(4,6).
arc(5,1).
arc(5,3).
arc(5,4).
arc(5,6).
arc(5,7).
arc(6,2).
arc(6,3).
arc(6,4).
arc(6,5).
arc(6,7).
arc(7,5).
arc(7,6).

%on met les couleurs aux noeuds (les couleurs sont des chiffres, il y en a au plus nb noeud)
{couleur(N, C)} :- noeud(N), n(C).

%on garde uniquement les ensembles avec 7 noeuds coloriés
:- {couleur(_, _)}Nb-1, nbNoeud(Nb).
:- Nb+1{couleur(_, _)}, nbNoeud(Nb).

%il y a forcement aucun doublons
:- couleur(N, C1), couleur(N, C2), C1<C2.

%on garde les noeuds tels que 2 voisins n'ont pas la même couleurs
:- arc(N1,N2), couleur(N1, C), couleur(N2, C).

% maintenant qu'on a toutes les solutions possibles, on cherche celles avec le minimum de couleurs, on se rend compte que le nombre de couleurs minimal est de 4 pour résoudre le graphe donné dans le sujet
cols(C) :- couleur(_,C).

1{res(1..X)}1 :- nbNoeud(X).

#minimize{N:res(N)}.

:- N+1{cols(_)}, res(N).
%ca marche avec 4 (en effet, si on supprime tous les ensembles de 5 couleurs ou plus, c'est satisfiable)














