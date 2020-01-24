/**
 * 
 */
package gestionRessources;

import Package1.interfaces.IBanque;
import Package1.interfaces.IRessource;
import gestionEtatdujeu.Etat;
import gestionBO.Objectif;
import java.util.Set;

/** 
* <!-- begin-UML-doc -->
* <!-- end-UML-doc -->
* @author Antoine Cadiou
* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
*/
public class Banque implements IBanque {
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private Etat etat;
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private Objectif objectif;
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private Set<Ressource> ressources;

	/** 
	* (non-Javadoc)
	 * @return 
	* @see IBanque#getRessources()
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public IRessource getRessources() {
		return null;
		// begin-user-code
		// TODO Module de remplacement de m�thode auto-g�n�r�

		// end-user-code
	}
}