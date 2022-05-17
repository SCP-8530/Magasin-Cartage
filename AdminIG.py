###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe AdminIG
###########################################################################

###################
### IMPORTATION ###
###################
import INTERFACEGRAPHIQUE.PY.Admin as Admin
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from GLOBAL import Global
##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################

#################
### PROGRAMME ###
#################
class gui(QtWidgets.QDialog, Admin.Ui_Dialog):
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
        
    
    ###########
    # METHODE #
    ###########  

    ######################
    # Bouton et ComboBox #
    ######################
    @pyqtSlot()
    def on_comboBoxType_changed(self):
        """
        Change le type d'object afficher et affecter par les boutons
        """
        #recupere l'entre de la combobox
        EntryCB = self.combo
        
    
    @pyqtSlot()
    def on_buttonNouveauCompte_clicked(self):
        """
        Ouvre la page de creation d'un nouvelle utilisateur
        """
        self.close()