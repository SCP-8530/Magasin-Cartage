###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Fichier Main
###########################################################################

###################
### IMPORTATION ###
###################
#importation de python
import sys
import json
from PyQt5 import QtWidgets

#importation du projet
import MainIG
import GLOBAL as G
import CLASSE.Potion as P
import CLASSE.PierreMagique as PM
import CLASSE.Sortillege as S
import CLASSE.Client as C

###############################
### DECLARATION DE FONCTION ###
###############################
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
    G.Global["CLIENT"].Deserialise(dictSave)

def MAJInventaire() -> None:
    """
    recupere tout les produit creer pour les mettre dans l'inventaire
    """
    #reset de l'inventaire
    G.Global["INVENTAIRE"] = []
    
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
            Art = P.Potion()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = str(ArticleSave["Quantite"])
            Art.Prix = str(ArticleSave["Prix"])
            Art.EffetPotion = ArticleSave["Effet Potion"]
            Art.DureePotion = ArticleSave["Duree Potion"]

            #mettre dans l'inventaire
            G.Global["INVENTAIRE"].append(Art)
        ##sortillege
        elif ArticleSave["Type"] == "Sortillege":
            Art = S.Sortillege()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = str(ArticleSave["Quantite"])
            Art.Prix = str(ArticleSave["Prix"])
            Art.EffetSortillege = ArticleSave["Effet Sortillege"]
            Art.EnergieNecessaire = ArticleSave["Energie Necessaire"]
            Art.SacrificeNecessaire = ArticleSave["Sacrifice Necessaire"]

            #mettre dans l'inventaire
            G.Global["INVENTAIRE"].append(Art)
        ##pierre magique
        elif ArticleSave["Type"] == "Pierre Magique":
            Art = PM.PierreMagique()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = str(ArticleSave["Quantite"])
            Art.Prix = str(ArticleSave["Prix"])
            Art.EnergiePierre = ArticleSave["Energie Pierre"]

            #mettre dans l'inventaire
            G.Global["INVENTAIRE"].append(Art)

def MAJFacture() -> None:
    """
    recupere toute les facture et mettre a jour les donne global
    """
    #importation
    import CLASSE.Facture as F

    #reset de l'inventaire
    G.Global["FACTURE"] = []
    
    #recupere la liste des ID
    tf = open("DATACENTER/Factures/raccourci.txt","r")
    LstFactureID = tf.read().splitlines()
    tf.close

    #instancier les different article dans l'inventaire
    for index in LstFactureID:
        #recupere la sauvegarde de l'article
        tf = open(f"DATACENTER/Factures/{index}.json")
        FactureSave = json.load(tf, object_hook=dict)
        tf.close()

        #instencie l'objet
        Fact = F.Facture()
        Fact.Deserialise(FactureSave)

        #mettre dans la liste
        G.Global["FACTURE"].append(Fact.__str__(p_bool=True))

def InstancieClient(p_dict={}) -> object:
    """
    Creer un objet client.
    (Fonction creer juste pour eviter un bug de boucle)

    :param p_dict: dict
    """
    c = C.Client()
    c.Deserialise(p_dict)
    return c

def MAJUtilisateur() -> list:
    """
    Recupere tout les utilisateur et en fait un liste d'objet
    """
    #valeur a return
    lstUser = []

    #recuperation des raccourcis
    tf = open("DATACENTER/User/raccourci.txt","r")
    lstRaccourciUser = tf.read().splitlines()
    tf.close

    #creer la liste
    for index in lstRaccourciUser:
        tf = open(f"DATACENTER/User/{index}.json","r")
        UserDict = json.load(tf,object_hook=dict)
        tf.close
        #instantation de l'objet
        user = C.Client()
        user.Deserialise(UserDict)

        lstUser.append(user)

    return lstUser

def MajArticleLst() -> list:
    """
    Recupere une list des Id des article
    """
    #recuperation des raccourcis
    tf = open("DATACENTER/Article/raccourci.txt","r")
    lstRaccourciArticle = tf.read().splitlines()
    tf.close

    return lstRaccourciArticle

def FactureCreate(p_dict={}) -> object:
    """
    Cree une facture a parti d'un dictionnaire
    
    :param p_dict: dict
    """
    #importation
    import CLASSE.Facture as F

    f = F.Facture()
    f.Deserialise(p_dict)

    return f
 
#################
### PROGRAMME ###
#################

#Demarrage de l'application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MainIG.gui()
    form.show()
    app.exec()