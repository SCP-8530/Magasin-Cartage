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
from GLOBAL import *
import MainIG
import sys
from PyQt5 import QtWidgets
from CLASSE import Potion, Sortillege, PierreMagique, Facture, Client 
##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################
def Main() -> None:
    """
    Ouvre la page principal du magasin
    """
    app = QtWidgets.QApplication(sys.argv)
    form = MainIG.gui()
    form.show()
    app.exec()

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
        user = Client.Client()
        user.Prenom = UserDict["Prenom"]
        user.Identifiant = UserDict["Identifiant"]
        user.MDP = UserDict["MDP"]
        user.Credit = str(UserDict["Credit"])
        user.LstFacture = UserDict["LstFacture"]

        lstUser.append(user)

    return lstUser

def MAJFacture() -> None:
    """
    recupere toute les facture et mettre a jour les donne global
    """
    #reset de l'inventaire
    Global["FACTURE"] = []
    
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
        Fact = Facture.Facture()
        Fact.Numero = FactureSave["Numero"]
        Fact.Date = FactureSave["Date"]
        Fact.LstArticle = FactureSave["LstArticle"]
        Fact.Client = FactureSave["Client"]

        #mettre dans la liste
        Global["FACTURE"].append(Fact.__str__())
#################
### PROGRAMME ###
#################

#Demarrage de l'application
if __name__ == "__main__":
    Main()