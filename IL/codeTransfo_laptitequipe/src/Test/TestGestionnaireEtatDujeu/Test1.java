package Test.TestGestionnaireEtatDujeu;

import static org.junit.Assert.assertEquals;

import java.util.HashSet;
import java.util.Set;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import Test.TestGestionnaireEtatDujeu.Bouchon.B_Banque;
import Test.TestGestionnaireEtatDujeu.Bouchon.B_Entite;

import gestionEtatdujeu.EntiteConcrete;
import gestionEtatdujeu.Etat;
import gestionEtatdujeu.GestionnaireEtatdujeu;

public class Test1 {
	
	GestionnaireEtatdujeu g= null;
	Set<EntiteConcrete> entites = null;
	@Before
	public void init() {	
		B_Banque banque = new B_Banque();
		entites = new HashSet<>();
		B_Entite e = new B_Entite("Soldat");
		entites.add(e);
		Etat etat = new Etat(banque,entites);
		g = new GestionnaireEtatdujeu(banque,etat);
		etat.setGestionnaireEtatdujeu(g);
	}
	@Test
	public void test1() {
		assertEquals(g.getiBanque().getRessources().getMontant(),new Integer(500));
	}
	
	@After
	public void end() {
		if(entites !=null)
			entites.clear();
	}
}
