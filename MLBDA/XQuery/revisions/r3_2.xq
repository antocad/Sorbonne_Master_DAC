
for $n in distinct-values(//joueur/nationalite)
let $nb := count(//joueur[nationalite = $n])
return <nationalite nom='{$n}' nb='{$nb}'/>

