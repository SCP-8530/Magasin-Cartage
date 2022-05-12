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
from INTERFACEGRAPHIQUE.PY import ConnectionPage
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
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
    form = ConnectionPageIG()
    form.show()
    app.exec()

def NouvelleUtilisateurPage():
    """
    Ouvre la page de creation d'un nouvelle utilisateur
    """
    app = QtWidgets.QApplication(sys.argv)
    form = ConnectionPageIG()
    form.show()
    app.exec()

def ConnectPage():
    """
    Ouvre la page de connection
    """
    app = QtWidgets.QApplication(sys.argv)
    form = ConnectionPageIG()
    form.show()
    app.exec()

#############################
### DECLARATION DE CLASSE ###
#############################
class ConnectionPageIG(QtWidgets.QDialog, ConnectionPage.Ui_Dialog):
    """
    Demarre l'application par une page de connection
    """
    ################
    # Constructeur #
    ################
    def __init__(self, parent=None):
        super(ConnectionPageIG, self).__init__(parent)
        self.setupUi(self)
        #customisation
        self.setWindowsTitle("Page de Connection")
    
    ##########
    # Bouton #
    ##########
    @pyqtSlot()
    def on_buttonConnection_clicked(self):
        """
        Connecte un utilisateur si il rentre le bon identifiant et MDP
        """
        Main()
        self.close()
    
    @pyqtSlot()
    def on_buttonNouveauCompte_clicked(self):
        """
        Ouvre la page de creation d'un nouvelle utilisateur
        """
        NouvelleUtilisateurPage()
        self.close()

#################
### PROGRAMME ###
#################
if __name__ == "__main__":
    ConnectPage()