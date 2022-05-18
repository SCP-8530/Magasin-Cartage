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
import json
from CLASSE.PierreMagique import PierreMagique
from CLASSE.Potion import Potion
from CLASSE.Sortillege import Sortillege
from CLASSE.Client import Client
import INTERFACEGRAPHIQUE.PY.Admin as Admin
from MainIG import MAJInventaire
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from GLOBAL import Global
from main import MAJUtilisateur
##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################
def IDLstArticle(p_test):
    for index in Global["INVENTAIRE"]:
        if p_test == index.ArticleID:
            return True
    return False

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
        self.HideLabel
        self.LabelVisibiliterPrime()
        
    
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
            self.buttonAjouter.setEnabled(True)
            self.buttonModifier.setEnabled(True)
            self.buttonSupprimer.setEnabled(True)

            #Activation des labels en dessous
            self.LabelVisibiliterArticle()
        elif EntryCB == "Utilisateur":
            #activation des boutons
            self.buttonAjouter.setDisabled(True)
            self.buttonModifier.setDisabled(True)
            self.buttonSupprimer.setEnabled(True)
        else:
            #activation des boutons
            self.buttonAjouter.setDisabled(True)
            self.buttonModifier.setDisabled(True)
            self.buttonSupprimer.setDisabled(True)
        
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

    def Erreur(self,p_code):
        """
        gere le message d'erreur
        """
        #afficher l'erreur
        self.labelErreur.show()
        #raccourcis
        le = self.labelErreur
        if p_code == 1:
            le.setText("* Identifiant inexistant")
        if p_code == 2:
            le.setText("* Identifiant deja existant veuillez en trouver un autre")
        if p_code == 3:
            le.setText("* Le nom n'est pas valide")
        if p_code == 4:
            le.setText("* L'ID n'est pas valide")
        if p_code == 5:
            le.setText("* La quantite n'est pas valide")
        if p_code == 6:
            le.setText("* Le nombre de credit n'est pas valide")
        if p_code == 7:
            le.setText("* L'energie de la pierre n'est pas valide")
        if p_code == 8:
            le.setText("* La duree de la potion n'est pas valide")
        if p_code == 9:
            le.setText("* Les effets de la potion n'est pas valide")
        if p_code == 10:
            le.setText("* L'energie Necessaire n'est pas valide")
        if p_code == 11:
            le.setText("* Les effets du sortillege n'est pas valide")
        if p_code == 12:
            le.setText("* Le sacrifice necessaire n'est pas valide")

    
    ######################
    # Bouton et ComboBox #
    ######################
    def on_comboBoxType_currentTextChanged(self):
        """
        Change le type d'object afficher et affecter par les boutons
        """
        self.LabelVisibiliterPrime()
        self.textBrowserObjet.setText("")
        #changement du titre et du textBrowser
        if self.comboBoxType.currentText() == "Article":
            #affichage des article
            self.labelTitle.setText("Liste des Articles:")
            for index in Global["INVENTAIRE"]:
                self.textBrowserObjet.append(index)       
        elif self.comboBoxType.currentText() == "Utilisateur":
            #affichage des utilisateur
            self.labelTitle.setText("Liste des Utilisateur:")
            #recuperation de la liste des objet Client puis affichage
            LstUser = MAJUtilisateur()
            for index in LstUser():
                self.textBrowserObjet.append(index.__str__())
        elif self.comboBoxType.currentText() == "Facture":
                 

 
    def on_comboBox4_currentTextChanged(self):
        """
        Changer les objets des articles
        """
        self.LabelVisibiliterArticle()    
    
    @pyqtSlot()
    def on_buttonAjouter_clicked(self):
        """
        Ajouter un article
        """
        #reset erreur
        self.labelErreur.hide()

        #voir si l'ID est valide
        if IDLstArticle(self.lineEditID.text()) == True:
            self.Erreur(2)
        #voir les autres erreur
        else:
            #recuperer le type
            EntryCB = self.comboBox4.currentText()

            #creer l'article
            Art = ""
            if EntryCB == "Pierre Magique":
                #recupere les valeurs
                Art = PierreMagique()
                Art.ArticleName = self.lineEdit1.text()
                Art.ArticleID = self.lineEditID.text()
                Art.Quantite = self.lineEdit2.text()
                Art.Prix = self.lineEdit3.text()
                Art.Type = "Pierre Magique"
                Art.EnergiePierre = self.lineEdit5.text()

                #verifier les erreurs propre au type
                if Art.EnergiePierre == "":
                    self.Erreur(7)
                
            elif EntryCB == "Potion":
                #recuperer les valeurs
                Art = Potion()
                Art.ArticleName = self.lineEdit1.text()
                Art.ArticleID = self.lineEditID.text()
                Art.Quantite = self.lineEdit2.text()
                Art.Prix = self.lineEdit3.text()
                Art.Type = "Potion"
                Art.DureePotion = self.lineEdit5.text()
                Art.EffetPotion = self.textEdit6.toPlainText()

                #verifier les erreurs propre au type
                if Art.DureePotion == "":
                    self.Erreur(8)
                elif Art.EffetPotion == "":
                    self.Erreur(9)

            elif EntryCB == "Sortillege":
                #recuperer les valeurs
                Art = Sortillege()
                Art.ArticleName = self.lineEdit1.text()
                Art.ArticleID = self.lineEditID.text()
                Art.Quantite = self.lineEdit2.text()
                Art.Prix = self.lineEdit3.text()
                Art.Type = "Sortillege"
                Art.EnergieNecessaire = self.lineEdit5.text()
                Art.EffetSortillege = self.textEdit6.toPlainText()
                Art.SacrificeNecessaire = self.textEdit7.toPlainText()

                #verifier les erreurs propre au type
                if Art.EnergieNecessaire == "":
                    self.Erreur(10)
                elif Art.EffetSortillege == "":
                    self.Erreur(11)
                elif Art.SacrificeNecessaire == "":
                    self.Erreur(12)

            
            #Verifier les erreur commun au cahque type
            if Art.ArticleName == "":
                self.Erreur(3)
            elif Art.ArticleID == "":
                self.Erreur(4)
            elif Art.Quantite == 0:
                self.Erreur(5)
            elif Art.Prix == 0.00:
                self.Erreur(6)

        #Si aucune erreur detecter sauvegarder
        if self.labelErreur.isHidden() == True:
            Art.Serialiser(Art.__dict__())
            MAJInventaire()

