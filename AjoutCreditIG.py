###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe AjoutCreditIG
###########################################################################

###################
### IMPORTATION ###
###################
from INTERFACEGRAPHIQUE.PY import AjoutCredit
from CLASSE.Client import Client
from GLOBAL import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################

#################
### PROGRAMME ###
#################
class gui(QtWidgets.QDialog, AjoutCredit.Ui_Dialog):
    """
    Demarre l'application par une page de connection
    """
    ################
    # Constructeur #
    ################
    def __init__(self, parent=None):
        super(gui, self).__init__(parent)
        self.setupUi(self)
        #customisation
        self.setWindowTitle("Creation de compte")
        self.labelErreur.hide()
    

    ##########
    # Bouton #
    ##########
    @pyqtSlot()
    def on_buttonAjoutCredit_clicked(self):
        """
        Ajout des credits a l'utilisateur
        """
        #reset erreur
        self.labelErreur.hide()

        #verifie que la valeur est une float
        valeur =  self.lineEditCredit.text()

        try:
            float(valeur)
        except ValueError:
            self.labelErreur.show()
        else:
            #ajouter les credit au client
            credit = Global["CLIENT"].Credit
            credit += float(valeur)
            Global["CLIENT"].Credit = str(credit)
            Global["DIALOG ACTIF"] = False
            self.close()        

        
        
    