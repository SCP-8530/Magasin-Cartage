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
from CLASSE import Client as C
from INTERFACEGRAPHIQUE.PY import NewUserPage
from GLOBAL import RACCOURCIS
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
        self.ResetErreur()
    
    ###########
    # Methode #
    ###########
    def ResetErreur(self) -> None:
        """
        Cache toute les erreurs
        """
        self.labelErreur1.hide()
        self.labelErreur2.hide()
        self.labelErreur3.hide()
        self.labelErreur4.hide()
        self.labelErreur5.hide()

    ##########
    # Bouton #
    ##########
    @pyqtSlot()
    def on_buttonNewUser_clicked(self):
        """
        Creer un nouvelle utilisateur
        """
        #reset les erreurs
        self.ResetErreur()

        #creer le nouveau compte
        Client = C.Client()

        Client.Prenom = self.lineEditPrenom.text()
        Client.Identifiant = self.lineEditIdentifiant.text()
        Client.MDP = self.lineEditMDP.text()
        Client.Credit = self.lineEditCredits.text()

        #verifie que tout es correct
        ErreurDetecter = False

        ##nom pas valide
        if Client.Prenom == "": 
            self.labelErreur1.show()
            ErreurDetecter = True
        ##identifant pas valide
        if Client.Identifiant == "": 
            self.labelErreur2.show()
            ErreurDetecter = True
        ##identifant deja existant
        if Client.Identifiant in RACCOURCIS(): 
            self.labelErreur2.show()
            ErreurDetecter = True
        ##mot de pass non valide
        if Client.MDP == "": 
            self.labelErreur3.show()
            ErreurDetecter = True
        ##mot de passe pas identique
        if self.lineEditMDP.text() != self.lineEditMDPConfirmation.text(): 
            self.labelErreur4.show()
            ErreurDetecter = True
        ##credit non valide
        if Client.Credit == 0.00:
            if self.lineEditCredits.text() != "0":
                self.labelErreur5.show()
                ErreurDetecter = True

        #fermer la fenetre si aucune erreur est detecter et aussi sauvegarde le compte
        if ErreurDetecter == False:
            Client.Serialisation(New=True)
            self.close()

        
        
    