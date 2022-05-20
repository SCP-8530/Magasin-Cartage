###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Fichier qui gere les valeurs Global et les fonctions de ses valeurs
###########################################################################

#################
### PROGRAMME ###
#################
from CLASSE import Client, Potion,Sortillege,PierreMagique
import json

Global = {
    "ID" : "",
    "CLIENT" : Client.Client(),
    "ADMIN" : ["CR2429","FC2000"],
    "INVENTAIRE" : [],
    "FACTURE" : [],
    "DIALOG ACTIF": False
    }

def RACCOURCIS() -> list:
    """
    Prepare la liste de tout les identifiant sauvegarder
    """
    tf = open("DATACENTER/User/raccourci.txt", "r")
    r = tf.read().splitlines()
    tf.close

    return r


def fCLIENT(p_identifiant="") -> None:
    """
    generer un client sauvegarder

    :param p_identifiant: str
    """
    #recuperer la sauvegarde
    tf = open(f"DATACENTER/User/{p_identifiant}.json")
    dictSave = json.load(tf, object_hook=dict)
    tf.close

    #ajouter les caracteristique du client a la valeur GLOBAL
    Global["CLIENT"].Prenom = dictSave["Prenom"]
    Global["CLIENT"].Identifiant = dictSave["Identifiant"]
    Global["CLIENT"].MDP = dictSave["MDP"]
    Global["CLIENT"].Credit = str(dictSave["Credit"])
    Global["CLIENT"].LstFacture = dictSave["LstFacture"]

def MAJInventaire() -> None:
    """
    recupere tout les produit creer pour les mettre dans l'inventaire
    """
    #reset de l'inventaire
    Global["INVENTAIRE"] = []
    
    #recupere la liste des ID
    tf = open("DATACENTER/Article/raccourci.txt","r")
    LstArticleID = tf.read().splitlines()
    tf.close

    #instancier les different article dans l'inventaire
    for index in LstArticleID:
        #recupere la sauvegarde de l'article
        tf = open(f"DATACENTER/Article/{index}.json")
        ArticleSave = json.load(tf, object_hook=dict)
        tf.close()

        #instencie l'objet
        ##potion
        if ArticleSave["Type"] == "Potion":
            Art = Potion.Potion()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = str(ArticleSave["Quantite"])
            Art.Prix = str(ArticleSave["Prix"])
            Art.EffetPotion = ArticleSave["Effet Potion"]
            Art.DureePotion = ArticleSave["Duree Potion"]

            #mettre dans l'inventaire
            Global["INVENTAIRE"].append(Art)
        ##sortillege
        elif ArticleSave["Type"] == "Sortillege":
            Art = Sortillege.Sortillege()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = str(ArticleSave["Quantite"])
            Art.Prix = str(ArticleSave["Prix"])
            Art.EffetSortillege = ArticleSave["Effet Sortillege"]
            Art.EnergieNecessaire = ArticleSave["Energie Necessaire"]
            Art.SacrificeNecessaire = ArticleSave["Sacrifice Necessaire"]

            #mettre dans l'inventaire
            Global["INVENTAIRE"].append(Art)
        ##pierre magique
        elif ArticleSave["Type"] == "Pierre Magique":
            Art = PierreMagique.PierreMagique()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = str(ArticleSave["Quantite"])
            Art.Prix = str(ArticleSave["Prix"])
            Art.EnergiePierre = ArticleSave["Energie Pierre"]

            #mettre dans l'inventaire
            Global["INVENTAIRE"].append(Art)
