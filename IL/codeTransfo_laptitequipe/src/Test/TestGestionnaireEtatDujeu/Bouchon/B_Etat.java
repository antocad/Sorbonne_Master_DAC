package Test.TestGestionnaireEtatDujeu.Bouchon;

import java.util.HashSet;
import java.util.Set;

import Package1.interfaces.IEtat;
import Package1.interfaces.IPrerequis;

public class B_Etat implements IEtat {

	@Override
	public Set<String> verifierPrerequis(IPrerequis prerequis) {
		Set<String> mySet = new HashSet<String>();
		return mySet;
	}

}
