/**
 * 
 */
package Package1.interfaces;

/** 
 * <!-- begin-UML-doc -->
 * <!-- end-UML-doc -->
 * @author Antoine Cadiou
 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
 */
public interface IRegles {
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @return
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public IEtat getEtatInitial();

	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @param who
	* @return
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	public IPrerequis getPrerequis(String who);
}