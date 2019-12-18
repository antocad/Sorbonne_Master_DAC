/*CADIOU Antoine 3670631
ORLUC Thomas 3670355*/


/*
________________________________________________________________________________
Exercice 1 (mis à jour)*/

subs(chat,felin).
subs(lion,felin).
subs(chien,canide).
subs(canide,chien).
subs(souris,mammifere).
subs(felin,mammifere).
subs(canide,mammifere).
subs(mammifere,animal).
subs(canari,animal).
subs(animal,etreVivant).
subs(and(animal,plante),nothing).
subs(and(plante,animal),nothing).
subs(lion,carnivoreExc).
subs(carnivoreExc,predateur).
subs(animal,some(mange)).
subs(carnivoreExc,all(mange,animal)).
subs(herbivoreExc,all(mange,plante)).
subs(_,not(and(all(mange,_),all(mange,nothing)))).
subs(pet,animal).
subs(all(aMaitre, _), pet).
subs(pet, some(aMaitre, _)).
subs(_, all(aMaitre,humain)).
subs(chihuahua, and(pet,chien)).
subs(felix,chat).
subs(felix,all(aMaitre, pierre)).
subs(pierre,humain).
subs(princesse,chihuahua).
subs(princesse, all(aMaitre,marie)).
subs(marie,humaine).
subs(jerry,souris).
subs(titi,canari).
subs(felix, all(mange, and(jerry, titi))).

/*
________________________________________________________________________________
Exercice 2

Q1) La règle 1 traduit la reflexivité, la regle 3 traduit la transitivité

Q3) la requete chien souris boucle a cause des regles chien/canide et canide/chien
Pour y remédier, on s'empêche de réutiliser un élément déjà rencontré
au cours des étapes précédentes de la preuve de subsomption:*/

subsS(C,D) :- subsS(C,D,[C]).
subsS(C,C,_).
subsS(C,D,_) :- subs(C,D), C\==D.
subsS(C,D,L) :- subs(C,E), not(member(E,L)), subsS(E,D,[E|L]), E\==D.

/*
Q7)
on s'attend à ce que cette requête nous montre tous les X qui subsument chat
soit: chat, felin, mammifere, animal, etreVivant, mais aussi mange.

?- subsS(chat,X).
X = chat ;
X = felin ;
X = mammifere ;
X = animal ;
X = etreVivant ;
false.

on s'attend à ce que cette requête nous montre tous les X qui sont subsumés par mammifere
soit: mammifere, chat, lion, felin, chien, canide, souris.

?- subsS(X,mammifere).
X = mammifere ;
X = souris ;
X = felin ;
X = canide ;
X = chat ;
X = lion ;
X = chien ;
false.
*/

equiv(X,Y) :- subs(X,Y),subs(Y,X).
equiv(carnivoreExc, all(mange, animal)).
equiv(herbivoreExc, all(mange, plante)).


/*
Q10) On a plus interet a dériver subsS(A,B) car on regarde de manière récursifs dans les concepts,
    nous pouvons donc répondre a toute requete atomique.
*/

/*Exercice 3*/
:- discontiguous subsS/3.
subsS(C,and(D1,D2),L) :- D1\=D2, subsS(C,D1,L), subsS(C,D2,L).
subsS(C,D,L) :- subs(and(D1,D2),D), E=and(D1,D2), not(member(E,L)), subsS(C,E,[E|L]), E\==C.
subsS(and(C,C),D,L) :- nonvar(C),subsS(C,D,[C|L]).
subsS(and(C1,C2),D,L) :- C1\=C2, subsS(C1,D,[C1|L]).
subsS(and(C1,C2),D,L) :- C1\=C2, subsS(C2,D,[C2|L]).
subsS(and(C1,C2),D,L) :- subs(C1,E1), E=and(E1,C2), not(member(E,L)), subsS(E,D,[E|L]),E\==D.
subsS(and(C1,C2),D,L) :- Cinv=and(C2,C1), not(member(Cinv,L)), subsS(Cinv,D,[Cinv|L]).

/*Numérotons les regles de 1 a 7
1- Si C peut etre subsumé par D1 et par D2, avec D1\=D2, il est a la fois l'un et l'autre. Par exemple
	subsS(chihuahua, and(pet,chien)). où un chihuahua est un chien et un animal de compagnie ne marcherais
	pas sans cette regle.
2-Si D subsume D1 et D2, qui eux même subsument C, alors D subsume C
	cela permet de valider subsS(and(chat,felin),mammifere)
3-Si C est subsumé par D, alors C et C sont subsumés par D.
	cela permet par exemple de valider subS(and(chat,chat),felin).
4/5- Ces regles permettent de valider le cas ou un D est subsumé par deux éléments. Si l'un de ces
	elements est subsumé par un autre, mettons C, alors D est subsumé par C, peut importe le deuxieme
	element
	cela permet de valider subsS(and(canide,_),animal) avec n'importe quel type a la place de _
	(meme un n'existant pas)
6- Si D subsume deux concepts C1 et C2, et que C1 est subsumé par E1, il subsume aussi l'intersection E1 et C2
	Par exemple, pet subsumant animal et some(aMaitre), et chien étant subsumé par animal, cette
	regle valide subsS(and(some(aMaitre),chien),pet)
7- Cette regle permet d'établir la comutativité de l'intersection de deux concepts
	subsS(and(chien,some(aMaitre)),pet) est donc validée grace a cette regle, et la 6
*/


/*
________________________________________________________________________________
Exercice 4

Q1)
subsS(all(R,C),all(R,D),L) :- subsS(C,D,L).
La solution consiste à l'ajouter plutôt au niveau factuel (donc de s'orienter vers le prédicat subs).


Pour le comprendre, on s'intéresse à ce que faisait subsS avant d'ajouter cette règle.
Comme on l'a vu, il lui fallait, au bout de sa récursion, une subsomption factuelle comme cas de base sur lequel
s'appuyer. Or, dans certains cas, subsS ne parvient jamais à se rerouter vers une subsomption factuelle qui
corresponde à ce qu'on cherche. En particulier, si aucun concept ne subsume all(R,C), on n'a aucune chance.
Utiliser subs au lieu de subsS permet de définir la règle comme une "traduction syntaxique", un peu comme on l'a
fait avec l'équivalence. */

:-discontiguous subs/2.
subs(all(R,C), all(R,D)):-subs(C,D).

/*
Q2)
?- subsS(lion, all(mange, etreVivant)).
true . -- Aurait été gérable via subsS.

?- subsS(all(mange, canari), carnivoreExc).
true . -- Nécessitait d'ajouter une règle au niveau factuel.

Q3)
L'idée est de faire comprendre à Prolog ce que c'est que ce nothing qui n'apparaît pour l'instant que dans
subs(and(animal, plante), nothing)

On s'oriente en fait vers une réécriture des requêtes données. Pour la première, on cherche à montrer
subsS(and(carnivoreExc,herbivoreExc),all(mange,nothing)),
donc subsS(and(all(mange,animal),all(mange,plante)),all(mange,nothing)).

Pour ce faire, on doit déjà traduire subs(and(animal, plante), nothing)
par subsS(all(mange, and(animal, plante)), all(mange, nothing)),
ce qui rappelle à notre bon souvenir les règles écrites pour l'intersection.

D'un autre côté, on voudrait bien que and(carnivoreExc, herbivoreExc)
soit subsumé par all(mange, and(animal, plante)), qui avec la subsomption précédente
doit permettre de déduire exactement ce qu'on veut.
D'où les ajouts: */

:- discontiguous subsS/3.
subsS(C, all(R, and(D1, D2)), L) :- D1 \= D2, subsS(C, all(R, D1), L), subsS(C, all(R, D2), L).
subsS(C, all(R, D), L) :- subs(and(D1, D2), D), E = all(R, and(D1, D2)), not(member(E, L)), subsS(C, E, [E|L]), E\==C.


/*
Q5)
Si Prolog a pu nous dire que les souris mangeaient quelque chose sans même savoir vraiment ce que cela implique
(cf. 2.5) c'est qu'il est capable de considérer tout quantificateur existentiel de type some(R), où R est un rôle,
comme un concept atomique.
Puisqu'un rôle ne peut pas être qualifié en FL-, on ne peut pas avoir de variations syntaxiques. some(R) est donc
déjà géré de la façon la plus appropriée par les règles sur la subsomption atomique.

Q6)
Récapitulons : ce programme sait maintenant gérer des concepts atomiques, et entre eux des subsomptions et des
équivalences ; il a la possibilité de considérer des intersections et des quantificateurs universels, et d'en
dériver même pour répondre à une requête qui n'en contient pas.

La requête subsS(lion,X) va donner lion, felin, mammifere, animal,etreVivant, de par sa hiérarchie de Linné (...)
donnée dans les faits,
mais encore carnivoreExc, predateur, vu ce qu'on a dit du régime alimentaire du lion, aussi selon les faits,
some(mange), car tous les animaux mangent selon les faits,
all(mange,some(mange)), car tout ce qui mange mange quelque chose selon les faits,
puis finalement all(mange,animal) par équivalence avec le régime carnivore,
et par suite all(mange,etreVivant) par subsomption entre animal et etreVivant.
Sans tenir compte de l'ordre, tout concorde:
?- subsS(lion, X).
X = lion ;
X = felin ;
X = carnivoreExc ;
X = mammifere ;
X = animal ;
X = etreVivant ;
X = some(mange) ;
X = predateur ;
X = all(mange, animal) ;
X = all(mange, etreVivant) ;
X = all(mange, some(mange)) ;
false

La requête subsS(X,predateur) va déjà donner predateur, carnivoreExc.
Elle renvoie aussi lion, car le lion est défini comme carnivoreExc,
puis all(mange,animal) par équivalence avec carnivoreExc,
puis la série all(mange,mammifere), all(mange,felin), all(mange,canide), all(mange,chien), all(mange, chat),
all(mange, souris), all(mange, canari), all(mange, lion), qui correspond à tout ce qu'on peut subsumer par animal,
puis toute une liste d'intersections possibles hors et dans le all (à cause des règles fraîchement définies en 4.3).
?- subsS(X,predateur).
X = predateur ;
X = carnivoreExc ;
X = lion ;
X = all(mange, animal) ;
X = all(mange, chat) ;
X = all(mange, lion) ;
X = all(mange, chien) ;
X = all(mange, souris) ;
X = all(mange, felin) ;
X = all(mange, canide) ;
X = all(mange, mammifere) ;
X = all(mange, canari) ;
puis un temps d'arrêt : il y a une infinité d'intersections disponibles !
quelle que soit l'intersection fixée and(C,D), je pourrai toujours l'augmenter de and(and(C,D),C).
Prolog boucle indéfiniment jusqu'à ce qu'on lui demande de s'arrêter.

________________________________________________________________________________
Exercice 5

L'incomplétude de cet ensemble a été constatée plus haut, lorsque la requête subsS(chien,and(canide,canide))
a renvoyé false (là où la subsomption est en fait correcte). A supposer que personne n'ait remarqué ce détail,
on a ici appris à gérer les subsomptions de concepts atomiques,
puis les équivalences,
puis les intersections,
puis les quantificateurs universels sous leurs deux formes (all(rôle, concept) et all(rôle, instance)),
avant de décider qu'il était inutile de se mêler des quantificateurs existentiels
(pour la bonne raison qu'ils ressemblent syntaxiquement à des concepts atomiques, FL- interdisant d'écrire des
intersections, négations, ou quoi que ce soit d'autre qu'un rôle atomique sous le quantificateur some()).
Les cinq cas connus de la grammaire de FL- ont donc été couverts.
En outre, le programme est probablement adéquat - toute chose qu'il reconnaît comme juste l'est. */
