###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe FactureIG
###########################################################################

###################
### IMPORTATION ###
###################
import INTERFACEGRAPHIQUE.PY.FacturePage as FacturePage
from CLASSE.Facture import Facture as F
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
class gui(QtWidgets.QDialog, FacturePage.Ui_Dialog):
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
        self.setWindowTitle("Historique de Facture")
        self.ViewFacture()
    
    def ViewFacture(self):
        for index in Global["CLIENT"].LstFacture:
            tf = open(f"DATACENTER/Factures/{index}.json","r")
            dict_json = json.load(tf,object_hook=dict)
            tf.close
            Fact = F()
            Fact.Deserialise(dict_json)
            self.textBrowserFacture.append(Fact.__str__(p_dict=True))
    ##########
    # Bouton #
    ##########
    @pyqtSlot()
    def on_buttonClose_clicked(self):
        """
        Ferme la fenetre
        """
        self.close()        

        
        
    