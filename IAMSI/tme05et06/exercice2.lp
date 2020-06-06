taille(8).

num(1..T) :- taille(T).
T{queen(1..T, 1..T)}T :- taille(T).

:- queen(X,Y1), queen(X,Y2), Y1<Y2.
:- queen(X1,Y), queen(X2,Y), X1<X2.

:- queen(X1,Y1), queen(X2,Y2), num(N), X1+N==X2, Y1+N==Y2.
:- queen(X1,Y1), queen(X2,Y2), num(N), X1+N==X2, Y1-N==Y2.

% 92 solutions
% --------------------

%:- not queen(1,1).
% 4 solutions quand une reine se trouve nécessairement en 1,1
% --------------------

%:- queen(4,4).
% 84 solutions quand aucune reine ne se trouve en 4,4
% --------------------

% avec une taille d'échiquier de 9*9, il y a 352 solutions au problème des 8 dames 
% avec une taille d'échiquier de 10*10, il y a 724 solutions au problème des 8 dames

