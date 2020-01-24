/**
 * 
 */
package gestionEtatdujeu;

import Package1.interfaces.IBanque;
import Package1.interfaces.IEtat;

/** 
* <!-- begin-UML-doc -->
* <!-- end-UML-doc -->
* @author Antoine Cadiou
* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
*/
public class GestionnaireEtatdujeu {
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private IBanque iBanque;
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private IEtat etat;
	
	
	public GestionnaireEtatdujeu(IBanque banque ,IEtat etat ) {
		this.etat=etat;
		iBanque = banque;
	}


	public IBanque getiBanque() {
		return iBanque;
	}


	public IEtat getEtat() {
		return etat;
	}
	
	
	
}