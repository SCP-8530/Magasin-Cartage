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
    def HideLabel(self):
        """
        Cache tout les object sous les boutons
        """
        #cacher les label
        self.label1.hide()
        self.label2.hide()
        self.label3.hide()
        self.label4.hide()
        self.label5.hide()
        self.label6.hide()
        self.label7.hide()

        #cacher les lines edit
        self.lineEdit1.hide()
        self.lineEdit2.hide()
        self.lineEdit3.hide()
        self.lineEdit5.hide()

        #cacher les autres objets
        self.comboBox4.hide()
        self.textEdit6.hide()
        self.textEdit7.hide()

    def LabelVisibiliterPrime(self):
        """
        Observe la combobox de type et affiche les labels et autre object necessaire
        """
        #recupere l'entre de la combobox
        EntryCB = self.comboBoxType.currentText()

        #Activer et afficher les objects qui
        self.HideLabel() 
        if EntryCB == "Article":
            #activation des boutons
            self.buttonAjouter.setEnabled()
            self.buttonModifier.setEnabled()
            self.buttonSupprimer.setEnabled()

            #Activation des labels en dessous
            self.LabelVisibiliterArticle()
        elif EntryCB == "Utilisateur":
            #activation des boutons
            self.buttonAjouter.setDisabled()
            self.buttonModifier.setDisabled()
            self.buttonSupprimer.setEnabled()
        else:
            #activation des boutons
            self.buttonAjouter.setDisabled()
            self.buttonModifier.setDisabled()
            self.buttonSupprimer.setDisabled()
        
    def LabelVisibiliterArticle(self):
        """
        regler les autre objets sous les bouton (comme LabelVisibiliterPrime)
        """
        #afficher les labels de base
        self.label1.show()
        self.label2.show()
        self.label3.show()
        self.lineEdit1.show()
        self.lineEdit2.show()
        self.lineEdit3.show()
        
        #Modifier label principal
        self.label1.setText("Nom de l'article:")
        self.label2.setText("Quantite Disponible:")
        self.label3.setText("Prix de l'article:")

        #recuperer le type et montrer la selection du type
        self.label4.show()
        self.comboBox4.show()
        type = self.comboBox4.currentText()

        #mettre les objects celon le type
        if type == "Pierre Magique":
            #afficher
            self.label5.show()
            self.lineEdit5.show()

            #modifier label
            self.label5.setText("Energie de la pierre:")
        elif type == "Potion":
            #afficher
            self.label5.show()
            self.lineEdit5.show()
            self.label6.show()
            self.textEdit6.show()

            #modifier label
            self.label5.setText("Durer de la potion:")
            self.label6.setText("Effet de la potion:")
        else:
            #afficher
            self.label5.show()
            self.lineEdit5.show()
            self.label6.show()
            self.textEdit6.show()
            self.label7.show()
            self.textEdit7.show()

            #modifier label
            self.label5.setText("Energie necessaire:")
            self.label6.setText("Effet du sort:")
            self.label7.setText("Sacrifice necessaire:")

    ######################
    # Bouton et ComboBox #
    ######################
    def on_comboBoxType_changed(self):
        """
        Change le type d'object afficher et affecter par les boutons
        """
        self.LabelVisibiliterPrime()
        
    def on_comboBox4_changed(self):
        """
        Changer les objets des articles
        """
        self.LabelVisibiliterArticle()
        
    
    @pyqtSlot()
    def on_buttonNouveauCompte_clicked(self):
        """
        Ouvre la page de creation d'un nouvelle utilisateur
        """
        self.close()