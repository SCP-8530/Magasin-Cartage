=== MISE A JOUR DANS L'UML ===
---Date:06/05/2022---
Dans Article:
	Ajout PrixTotal()
	Modification de l'attribut articleRefNum en articleID

Dans Facture:
	Ajout de l'attribut Client
	Ajout de la methode dict
	Supretion de la methode AnnulerPaye

Dans Potion:
	Supretion de l'attribut nomPotion

Dans Sortillege:
	Supretion de l'attribut nomSortillege

Dans PierreMagique:
	Supretion de l'attribut nomPierreMagique

Dans Client:
	Ajout de la methode dict
	Ajout de la methode Serialisation
	Ajout de la methode Payer

---Date:06/05/2022---
Dans Client
    Supretion de l'attribut numeroClient #Utilisation de identifiant comme "numero"

---Date:17/05/2022---
Dans Article
	Ajout de l'attribut Type
	Ajout de la methode Serialiser

Dans Potion
	Ajout de la methode dict

Dans Sortillege
	Ajout de la methode dict

Dans PierreMagique
	Ajout de la methode dict

---Date:25/05/2022---
Dans Client
	Ajout de la methode dict
	Ajout de la methode Deserialise

Dans Facture
	Ajout de la methode Deserialise
	Ajout du parametre p_bool dans __str__
	Suppretion du parametre Client dans PayerFacture

Dans Article
	Modification du type de valeur retourner dans PrixTotal
	Ajout du parametre p_dict dans Serialiser
	Ajout du parametre New dans Serialiser
