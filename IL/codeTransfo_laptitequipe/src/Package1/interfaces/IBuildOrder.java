/**
 * 
 */
package Package1.interfaces;

import java.util.Set;

/** 
* <!-- begin-UML-doc -->
* <!-- end-UML-doc -->
* @author Antoine Cadiou
* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
*/
public interface IBuildOrder {
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @param regles
	* @param objectif
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public void createBO(IRegles regles, IObjectif objectif);

	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public void calculerBuildOrder();

	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @return
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public Set<IAction> getActions();
}