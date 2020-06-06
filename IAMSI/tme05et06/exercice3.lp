taille(9).
num(1..T) :- taille(T).
pos(0..T-1, 0..T-1) :- taille(T).
{case(V, X, Y)} :- num(V), pos(X, Y).
%on garde que les ensemble qui ont une case par position
:- pos(X,Y), not case(_,X,Y).
:- taille(T), T*T+1{case(_,_,_)}. %on restreint aux ensembles de taille T*T (utile?)

% --------------- Question 2

:- not case(7,0,1).
:- not case(6,0,3).
:- not case(3,0,5).
:- not case(1,0,7).
:- not case(4,0,8).
:- not case(8,1,0).
:- not case(9,1,4).
:- not case(6,2,1).
:- not case(3,2,2).
:- not case(2,2,3).
:- not case(1,2,4).
:- not case(8,2,6).
:- not case(3,3,4).
:- not case(5,3,7).
:- not case(9,3,8).
:- not case(6,4,0).
:- not case(8,5,8).
:- not case(5,6,1).
:- not case(8,6,3).
:- not case(3,6,8).
:- not case(4,7,0).
:- not case(1,7,2).
:- not case(3,7,3).
:- not case(6,7,4).
:- not case(2,7,5).
:- not case(7,7,6).
:- not case(8,7,7).
:- not case(3,8,0).
:- not case(6,8,2).
:- not case(1,8,3).
:- not case(9,8,6).
:- not case(2,8,8).

% --------------- Question 3
:- case(V,X,Y1), case(V,X,Y2), Y1<Y2. %contrainte sur les lignes
:- case(V,X1,Y), case(V,X2,Y), X1<X2. %contrainte sur les colonnes

%contrainte sur les blocs (plus compliquée)
nb(0..2).
ajout(X, Y) :- nb(X),nb(Y).
origine(Xo,Yo, B) :- case(_,X,Y), Xo=(X/3)*3, Yo=(Y/3)*3, B=(Xo+1)*(Xo+1)+Yo.
values(V, B, Xn,Yn) :- origine(Xo,Yo, B), ajout(Xadd, Yadd), Xn=Xo+Xadd, Yn=Yo+Yadd, case(V,Xn,Yn).
:- values(V, B, X1,Y1),values(V, B, X2,Y2), X1<X2.
:- values(V, B, X1,Y1),values(V, B, X2,Y2), Y1<Y2.


% --------------- Question 4
% solution unique: une case est au format (valeur,ligne,colonne)

% case(1,3,0) case(1,1,1) case(1,7,2) case(1,8,3) case(1,2,4) case(1,5,5) case(1,6,6) case(1,0,7) case(1,4,8) case(2,0,0) case(2,5,1) case(2,6,2) case(2,2,3) case(2,4,4) case(2,7,5) case(2,3,6) case(2,1,7) case(2,8,8) case(3,8,0) case(3,4,1) case(3,2,2) case(3,7,3) case(3,3,4) case(3,0,5) case(3,1,6) case(3,5,7) case(3,6,8) case(4,7,0) case(4,3,1) case(4,1,2) case(4,5,3) case(4,6,4) case(4,2,5) case(4,4,6) case(4,8,7) case(4,0,8) case(5,2,0) case(5,6,1) case(5,4,2) case(5,1,3) case(5,5,4) case(5,8,5) case(5,0,6) case(5,3,7) case(5,7,8) case(6,4,0) case(6,2,1) case(6,8,2) case(6,0,3) case(6,7,4) case(6,3,5) case(6,5,6) case(6,6,7) case(6,1,8) case(7,6,0) case(7,0,1) case(7,5,2) case(7,3,3) case(7,8,4) case(7,1,5) case(7,7,6) case(7,4,7) case(7,2,8) case(8,1,0) case(8,8,1) case(8,3,2) case(8,6,3) case(8,0,4) case(8,4,5) case(8,2,6) case(8,7,7) case(8,5,8) case(9,5,0) case(9,7,1) case(9,0,2) case(9,4,3) case(9,1,4) case(9,6,5) case(9,8,6) case(9,2,7) case(9,3,8)

% --------------- Question 5

% Si on supprime des chiffres naïvement de la grille de l'énoncé, on se rend compte qu'il y a plusieurs solutions possibles
% La méthode reste néamoins plus rapide et efficace qu'une solution basée sur du backtracking, car certaines grilles sont faites pour prolonger le backtrack, alors qu'ici ce n'est pas le cas. Si on utilise la grille suivante, on se rend compte que le résultat arrive directement alors qu'il mettrait plusieurs secondes en C. (grille anti-backtrack tirée de wikipedia).
/*
:- not case(3,1,5).
:- not case(8,1,7).
:- not case(5,1,8).
:- not case(1,2,2).
:- not case(2,2,4).
:- not case(5,3,3).
:- not case(7,3,5).
:- not case(4,4,2).
:- not case(1,4,6).
:- not case(9,5,1).
:- not case(5,6,0).
:- not case(7,6,7).
:- not case(3,6,8).
:- not case(2,7,2).
:- not case(1,7,4).
:- not case(4,8,4).
:- not case(9,8,8).
*/

