###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe ConnectionPageIG
###########################################################################

###################
### IMPORTATION ###
###################
from GLOBAL import Global, RACCOURCIS, fCLIENT
import INTERFACEGRAPHIQUE.PY.ConnectionPage as ConnectionPage
import NewUserPageIG
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
class gui(QtWidgets.QDialog, ConnectionPage.Ui_Dialog):
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
        self.setWindowTitle("Page de Connection")
        self.labelErreur.hide()
    
    ##########
    # Bouton #
    ##########
    @pyqtSlot()
    def on_buttonConnection_clicked(self):
        """
        Connecte un utilisateur si il rentre le bon identifiant et MDP
        """
        #reset erreur
        self.labelErreur.hide()

        #receperation des donnees
        LoginIdentifiant = self.lineEditIdentifiant.text()
        LoginMDP = self.lineEditMotDePasse.text()

        #tester la connection
        if RACCOURCIS().count(LoginIdentifiant) == 0:
            #identifiant n'existant pas
            self.lineEditIdentifiant.setText("")
            self.lineEditMotDePasse.setText("")
            self.labelErreur.show()
        else:
            fCLIENT(LoginIdentifiant)
            if Global["CLIENT"].MDP == LoginMDP:
                #identifiaction correct
                Global["ID"] = LoginIdentifiant
                self.close()
            else:
                #mauvaise mot de passe
                self.lineEditMotDePasse.setText("")
                self.labelErreur.show()

    
    @pyqtSlot()
    def on_buttonNouveauCompte_clicked(self):
        """
        Ouvre la page de creation d'un nouvelle utilisateur
        """
        #reset erreur
        self.labelErreur.hide()

        form = NewUserPageIG.gui()
        form.show()
        form.exec_()