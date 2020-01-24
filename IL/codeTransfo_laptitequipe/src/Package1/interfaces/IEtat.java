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
public interface IEtat {
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @param prerequis
	* @return
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public Set<String> verifierPrerequis(IPrerequis prerequis);
}