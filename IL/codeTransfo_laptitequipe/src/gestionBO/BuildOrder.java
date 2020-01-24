/**
 * 
 */
package gestionBO;

import Package1.interfaces.IBuildOrder;
import java.util.Set;
import Package1.interfaces.IObjectif;
import Package1.interfaces.IRegles;
import Package1.interfaces.IAction;

/** 
* <!-- begin-UML-doc -->
* <!-- end-UML-doc -->
* @author Antoine Cadiou
* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
*/
public class BuildOrder implements IBuildOrder {
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
	private Set<Action> actions;

	/** 
	* (non-Javadoc)
	* @see IBuildOrder#createBO(IRegles regles, IObjectif objectif)
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public void createBO(IRegles regles, IObjectif objectif) {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré

		// end-user-code
	}

	/** 
	* (non-Javadoc)
	* @see IBuildOrder#calculerBuildOrder()
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public void calculerBuildOrder() {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré

		// end-user-code
	}

	/** 
	* (non-Javadoc)
	* @see IBuildOrder#getActions()
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public Set<IAction> getActions() {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré
		return null;
		// end-user-code
	}
}