/*	ORLUC Thomas 3670355
	CADIOU Antoine 3670631 */

/*Exercice1*/
/*r(a,b).
r(f(X),Y) :- p(X,Y).
p(f(X),Y) :- r(X,Y).




Exercice 1
[trace]  ?- r(f(f(a)),b).
   Call: (7) r(f(f(a)), b) ? creep
   Call: (8) p(f(a), b) ? creep
   Call: (9) r(a, b) ? creep
   Exit: (9) r(a, b) ? creep
   Exit: (8) p(f(a), b) ? creep
   Exit: (7) r(f(f(a)), b) ? creep
true.


[trace]  ?- p(f(a),b).
   Call: (7) p(f(a), b) ? creep
   Call: (8) r(a, b) ? creep
   Exit: (8) r(a, b) ? creep
   Exit: (7) p(f(a), b) ? creep
true.


Il empile les étapes, jusqu'a trouver une clause existante, il dépile et remonte le resultat vrai a chaque étape.

*/








/*Exercice2*/
/*r(a,b).
q(X,X).
q(X,Z) :- r(X,Y),q(Y,Z).


Exercice 2

[trace]  ?- q(X,b).
   Call: (7) q(_G2809, b) ? creep
   Exit: (7) q(b, b) ? creep
X = b .

[trace]  ?- q(b,X).
   Call: (7) q(b, _G2810) ? creep
   Exit: (7) q(b, b) ? creep
X = b .

A cause de la clause q(X,X), si on ne spécifie pas deux variables, le programme va forcément arriver a X=b (ou si q(X,Y), X=Y)
*/


/*Exercice 3*/
/*r(X) :- s(X).
d(X) :- c(X).
e(X) :- r(X).
s(X) :- d(X).
c(p).
c(z).



Exercice 3
e(X)
En appuyant sur ; prolog donne bien les deux résultats, Pascal et Zoé.
*/


/*Exercice 4*/
/*pere(pepin,charlemagne).
pere(henri4,louis13).
pere(antoine,henri4).
pere(louis13,roisoleil).
pere(roisoleil,louisfrancois).
mere(berthe,charlemagne).
mere(annedautriche,roisoleil).
parent(X,Y) :- pere(X,Y).
parent(X,Y) :- mere(X,Y).
parent(X,Y,Z) :- pere(X,Z), mere(Y,Z).
frereOuSoeur(X,Y) :- pere(Z,X), pere(Z,Y).
frereOuSoeur(X,Y) :- mere(Z,X), mere(Z,Y).
grandPere(X,Y) :- pere(X,Z), parent(Z,Y).
ancetre(X,Y) :- parent(X,Y).
ancetre(X,Y) :- ancetre(X,Z), parent(Z,Y).
ancetre(X,Y) :- parent(X,Z), ancetre(Z,Y).



Exercice 4
Pour les appels récursifs, on s'apperçoit qu'il existe 2 clauses qui peuvent fonctionner (en plus du cas d'arrêt):
ancetre(X,Y) :- ancetre(X,Z), parent(Z,Y).
ancetre(X,Y) :- parent(X,Z), ancetre(Z,Y).

La trace est différente, et la deuxième semble plus optimisée.

si le cas d'arret se trouve après l'appel recursif alors il y a une boucle infinie des appels des clauses
*/

/*Exercice 5*/
et(0,0,0).
et(0,1,0).
et(1,0,0).
et(1,1,1).

ou(1,X,1).
ou(X,1,1).
ou(0,0,0).

non(0,1).
non(1,0).








