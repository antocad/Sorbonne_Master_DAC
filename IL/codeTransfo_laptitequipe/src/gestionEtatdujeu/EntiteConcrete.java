/**
 * 
 */
package gestionEtatdujeu;

import Package1.interfaces.IEntiteConcrete;
import gestionRegles.EntiteRegle;

/** 
* <!-- begin-UML-doc -->
* <!-- end-UML-doc -->
* @author Antoine Cadiou
* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
*/
public abstract class EntiteConcrete implements IEntiteConcrete {
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private String nom;
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private etatEntite etatEntite;
	/** 
	* <!-- begin-UML-doc -->
	* <!-- end-UML-doc -->
	* @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	*/
	private Integer tempRestant;
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
	private EntiteRegle entiteRegle;
	
	public EntiteConcrete (String nom) {
		this.nom=nom;
	}
	@Override
	public String getNom() {
		return nom;
	}
	public etatEntite getEtatEntite() {
		return etatEntite;
	}
	public void setEtatEntite(etatEntite etatEntite) {
		this.etatEntite = etatEntite;
	}
	public Integer getTempRestant() {
		return tempRestant;
	}
	public void setTempRestant(Integer tempRestant) {
		this.tempRestant = tempRestant;
	}
	public Etat getEtat() {
		return etat;
	}
	public void setEtat(Etat etat) {
		this.etat = etat;
	}
	public EntiteRegle getEntiteRegle() {
		return entiteRegle;
	}
	public void setEntiteRegle(EntiteRegle entiteRegle) {
		this.entiteRegle = entiteRegle;
	}
	
}