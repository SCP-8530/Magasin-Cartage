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
from collections import UserDict
from GLOBAL import *
import MainIG
import sys
from PyQt5 import QtWidgets
from CLASSE import Potion, Sortillege, PierreMagique 
##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################
def Main():
    """
    Ouvre la page principal du magasin
    """
    app = QtWidgets.QApplication(sys.argv)
    form = MainIG.gui()
    form.show()
    app.exec()

def MAJInventaire():
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
            Art.Quantite = ArticleSave["Quantite"]
            Art.Prix = ArticleSave["Prix"]
            Art.EffetPotion = ArticleSave["Effet Potion"]
            Art.DureePotion = ArticleSave["Duree Potion"]

            #mettre dans l'inventaire
            Global["INVENTAIRE"].append(Art)
        ##sortillege
        elif ArticleSave["Type"] == "Sortillege":
            Art = Sortillege.Sortillege()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = ArticleSave["Quantite"]
            Art.Prix = ArticleSave["Prix"]
            Art.EffetSortillege = ArticleSave["Effet Sortillege"]
            Art.EnergieNecessaire = ArticleSave["Energie Necessaire"]
            Art.SacrificeNecessaire = ArticleSave["Sacrifice Necessaire"]

            #mettre dans l'inventaire
            Global["INVENTAIRE"].append(Art)
        ##pierre magique
        elif ArticleSave["Type"] == "PierreMagique":
            Art = PierreMagique.PierreMagique()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = ArticleSave["Quantite"]
            Art.Prix = ArticleSave["Prix"]
            Art.EnergiePierre = ArticleSave["Energie Pierre"]

            #mettre dans l'inventaire
            Global["INVENTAIRE"].append(Art)

def MAJUtilisateur():
    """
    Recupere tout les utilisateur et en fait un liste d'objet
    """
    #valeur a return
    lstUser = []

    #recuperation des raccourcis
    tf = open("DATACENTER/User/raccourcis.txt","r")
    lstRaccourciUser = tf.read().splitlines()
    tf.close

    #creer la liste
    for index in lstRaccourciUser:
        tf = open(f"DATACENTER/User/{index}.json")
        UserDict = json.load(tf,object_hook=dict)
        tf.close
        #instantation de l'objet
        user = Client()
        user.Prenom = UserDict["Prenom"]
        user.Identifiant = UserDict["Identifiant"]
        user.MDP = UserDict["MDP"]
        user.Credit = UserDict["Credit"]
        user.LstFacture = UserDict["LstFacture"]

        lstUser.append(user)

    return lstUser
#################
### PROGRAMME ###
#################

#Demarrage de l'application
if __name__ == "__main__":
    Main()