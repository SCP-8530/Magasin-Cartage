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
import sys
import INTERFACEGRAPHIQUE.PY.MainPage as MainPage
import ConnectionPageIG
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from GLOBAL import IDENTIFIANT
##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################
def OuvrirConnectionPage():
    """
    gere la connection
    """
    while True:
        if IDENTIFIANT=="":
            form = ConnectionPageIG.gui()
            form.show()
            form.exec_()
        else:
            break

#################
### PROGRAMME ###
#################
class gui(QtWidgets.QMainWindow, MainPage.Ui_MainWindow):
    """
    Page principale de l'application
    """
    ################
    # Constructeur #
    ################
    def __init__(self, parent=None):
        super(gui, self).__init__(parent)
        self.setupUi(self)
        #customisation
        self.setWindowTitle("Page de Connection")
        self.labelErreur.hide()
        OuvrirConnectionPage()
    
    ###########
    # METHODE #
    ###########
    def ActivationBouton(self,p_etat):
        self.buttonAjouter.setEnabled(p_etat)
        self.buttonFacture.setEnabled(p_etat)
        self.buttonPayer.setEnabled(p_etat)
        self.buttonRetirer.setEnabled(p_etat)

    ##########
    # Bouton #
    ##########
    @pyqtSlot()
    def on_buttonConnection_clicked(self):
        """
        Connecte un utilisateur si il rentre le bon identifiant et MDP
        """
        self.close()
    
    @pyqtSlot()
    def on_buttonNouveauCompte_clicked(self):
        """
        Ouvre la page de creation d'un nouvelle utilisateur
        """
        self.close()