/*
ORLUC Thomas 3670355
CADIOU Antoine 3670631
*/
/*
Exercice 1:
*/
/*
[a, [b, c], d] = [X].
[a, [b, c], d] = [X, Y, Z].
[a, [b, c], d] = [ a | L].
[a, [b, c], d] = [X, Y].
[a, [b, c], d] = [X | Y].
[a, [b, c], d] = [a, b | L].
[a, b, [c, d]] = [a, b | L].
[a, b, c, d | L1] = [a, b | L2].
*/

/* Exercice 2: */

concatene([], L, L).
concatene([A|L1], L2, [A|L3]) :- concatene(L1,L2,L3).

%on utilise concatene pour recuperer le dernier element de L2, en essayant de le comparer avec le premier de L1
inverse([],[]).
inverse([A|L1], L2) :- inverse(L1,R), concatene(R,[A],L2).

supprime([], _, []).
supprime([X|L1], X, L2) :- supprime(L1, X, L2).
supprime([Y|L1], X, [Y|L2]) :- supprime(L1, X, L2).

filtre(L,[],L).
filtre(L1, [A|L2], L3) :- supprime(L1,A,R), filtre(R,L2,L3).

/*Exercice3*/

palindrome(L) :- inverse(L,L).
