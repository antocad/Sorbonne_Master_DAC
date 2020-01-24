



package Test.TestGestionnaireEtatDujeu.Bouchon;

import Package1.interfaces.IBanque;
import Package1.interfaces.IRessource;

public class B_Banque implements IBanque{
	IRessource r = new B_Ressource();
	@Override
	public IRessource getRessources() {
		return r;
	}
}
