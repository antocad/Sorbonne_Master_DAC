/**
 * 
 */
package gestionEtatdujeu;

import Package1.interfaces.IBanque;
import Package1.interfaces.IEtat;
import gestionRessources.Banque;
import java.util.Set;
import Package1.interfaces.IPrerequis;

/** 
* <!-- begin-UML-doc -->
* <!-- end-UML-doc -->
* @author Antoine Cadiou
* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
*/
public class Etat implements IEtat {
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private IBanque banque;
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private Set<EntiteConcrete> entites;
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private GestionnaireEtatdujeu gestionnaireEtatdujeu;

	public Etat (IBanque banque , Set<EntiteConcrete> entites , GestionnaireEtatdujeu gestionnaireEtatdujeu) {
		this.banque=banque;
		this.entites=entites;
		this.gestionnaireEtatdujeu=gestionnaireEtatdujeu;
	}
	
	public Etat (IBanque banque , Set<EntiteConcrete> entites ){
		this.banque=banque;
		this.entites=entites;
		this.gestionnaireEtatdujeu=null;
	}
	
	/** 
	* (non-Javadoc)
	* @see IEtat#verifierPrerequis(IPrerequis prerequis)
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public Set<String> verifierPrerequis(IPrerequis prerequis) {
		
		return null;
		// end-user-code
	}

	public void setGestionnaireEtatdujeu(GestionnaireEtatdujeu gestionnaireEtatdujeu) {
		this.gestionnaireEtatdujeu = gestionnaireEtatdujeu;
	}

	public IBanque getBanque() {
		return banque;
	}

	public Set<EntiteConcrete> getEntites() {
		return entites;
	}

	public void setEntites(Set<EntiteConcrete> entites) {
		this.entites = entites;
	}

	public GestionnaireEtatdujeu getGestionnaireEtatdujeu() {
		return gestionnaireEtatdujeu;
	}
}