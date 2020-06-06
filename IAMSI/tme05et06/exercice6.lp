nE(5). % nombre d'equipes
1{nS(1..X)}1 :- nE(NE), X=NE*(NE-1).

#minimize{N:nS(N)}.

equipe(1..X) :- nE(X).

% match(equipe1, equipe2, match_domicile/exterieur, mercredi/dimanche, semaine)
NE*(NE-1){match(E1, E2, 1..2, 1..2, 1..NS)}NE*(NE-1) :- nE(NE), nS(NS), equipe(E1), equipe(E2), E1<E2.

%j'enleve les equipes qui s'affrontent elles mêmes
:- match(E,E,_,_,_).

%j'enleve les symétries
:- match(E1,E2,_,_,_), match(E2,E1,_,_,_).

%on prend les ensembles où il y a le match à domicile ET le match retour
:- match(E1,E2,1,_,_), not match(E1,E2,2,_,_).
:- match(E1,E2,2,_,_), not match(E1,E2,1,_,_).

%il faut qu'une equipe ne fasse pas plus d'un match par jour
:- match(E1,_,D1,J,S), match(E1,_,D2,J,S), D1<D2.


% ----------------------- Question 2
pEXT(50).
pDOM(40).

a(X) :- pEXT(PEXT), nE(NE), X= PEXT*(NE-1)/100.
b(X) :- pDOM(PDOM), nE(NE), X= PDOM*(NE-1)/100.

:- {match(E,_,2,2,_)}A-1, a(A).
:- {match(_,E,2,2,_)}A-1, a(A).
%il doit y avoir plus de pEXT pourcent de matchs à l'exterieur les dimanches (donc si il y en a moins on prend pas en compte)

:- {match(E,_,1,2,_)}B-1, b(B).
:- {match(_,E,1,2,_)}B-1, b(B).
%il doit y avoir plus de pDOM pourcent de matchs à domicile les dimanches (donc si il y en a moins on prend pas en compte)

:- match(E,_,2,1,X), match(E,_,2,2,X), match(E,_,2,1,X+1).
:- match(E,_,2,2,X), match(E,_,2,1,X+1), match(E,_,2,2,X+1).
%aucune equipe ne joue strictement plus de deux matchs consecutifs à l exterieur

:- match(E,_,1,1,X), match(E,_,1,2,X), match(E,_,1,1,X+1).
:- match(E,_,1,2,X), match(E,_,1,1,X+1), match(E,_,1,2,X+1).
%aucune equipe ne joue strictement plus de deux matchs consecutifs à domicile

% ----------------------- Question 3
% j'ai rajouté l'option de minimization ci-dessus pour connaitre le nombre minimum de semaine nécessaire
% le nombre de jour minimum sera donc 2*nS (ou 2*nS -1 si on ne fait pas de match le dimanche de la dernière semaine)

% ----------------------- Question 4
% C'est beaucoup plus rapide que le code en python
