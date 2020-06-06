
(defrule my_init
	 (initial-fact)
=>
	(watch facts)
	(watch rules)

	(assert (rougeurs patient))
	(assert (peu_bouton patient))
	(assert (forte_fievre patient))
	(assert (froid patient))
	(assert (yeux_douloureux patient))
	(assert (amygdales_rouges patient))
	(assert (peau_pele patient))
	(assert (peau_seche patient))
)



(defrule eruption_cutanee_peu_bouton
	(peu_bouton ?x)
=>
	(assert (eruption_cutanee ?x))
)

(defrule eruption_cutanee_bcp_bouton
	(bcp_bouton ?x)
=>
	(assert (eruption_cutanee ?x))
)

(defrule exantheme_eruption_cutanee
	(eruption_cutanee ?x)
=>
	(assert (exantheme ?x))
)

(defrule exantheme_rougeurs
	(rougeurs ?x)
=>
	(assert (exantheme ?x))
)

(defrule febrile_forte_fievre
	(forte_fievre ?x)
=>
	(assert (febrile ?x))
)

(defrule febrile_froid
	(froid ?x)
=>
	(assert (febrile ?x))
)

(defrule signe_suspect
	(amygdales_rouges ?x)
	(rougeurs ?x)
	(peau_pele ?x)
=>
	(assert (signe_suspect ?x))
)

(defrule rougeole1
	(declare (salience -1000))
	(febrile ?x)
	(yeux_douloureux ?x)
	(exantheme ?x)
=>
	(assert (rougeole ?x))
)

(defrule rougeole2
	(declare (salience -1000))
	(signe_suspect ?x)
	(forte_fievre ?x)
=>
	(assert (rougeole ?x))
)

(defrule non_rougeole
	(declare (salience -1001))
	(peu_fievre ?x)
	(peu_bouton ?x)
	?r <- (rougeole ?x)
=>
	(retract ?r)
)

(defrule douleur_yeux
	(yeux_douloureux ?x)
=>
	(assert (douleur ?x))
)

(defrule douleur_dos
	(dos_douloureux ?x)
=>
	(assert (douleur ?x))
)

(defrule grippe
	(declare (salience -1000))
	(dos_douloureux ?x)
	(febrile ?x)
=>
	(assert (grippe ?x))
)



(defrule rubeole
	(declare (salience -1002))
	(not (rougeole ?x))
	(peau_seche ?x)
	(inflammation_ganglions ?x)
	(not (pustule ?x))
	(not (froid ?x))
=>
	(assert (rubeole ?x))
)

(defrule varicelle
	(declare (salience -1002))
	(not (rougeole ?x))
	(fortes_demangeaisons ?x)
	(pustules ?x)
=>
	(assert (varicelle ?x))
)

