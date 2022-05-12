###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe NewUserPageIG
###########################################################################

###################
### IMPORTATION ###
###################
from INTERFACEGRAPHIQUE.PY import NewUserPage
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
class gui(QtWidgets.QDialog, NewUserPage.Ui_Dialog):
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
    
    ##########
    # Bouton #
    ##########
    @pyqtSlot()
    def on_buttonNewUser_clicked(self):
        """
        Connecte un utilisateur si il rentre le bon identifiant et MDP
        """
        self.close()
    