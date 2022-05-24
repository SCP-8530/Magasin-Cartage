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
import os
from CLASSE.PierreMagique import PierreMagique
from CLASSE.Potion import Potion
from CLASSE.Sortillege import Sortillege
from CLASSE.Client import Client
import INTERFACEGRAPHIQUE.PY.Admin as Admin
from main import MAJFacture, MAJUtilisateur, MajArticleLst
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from GLOBAL import Global, MAJInventaire
##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################
def IDLstArticle(p_test="") -> bool:
    """
    Analyse les ID des article et voir si il sont la ou non

    :param p_test: str
    """
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
        self.setWindowTitle("Page Admin")
        self.labelErreur.hide()
        self.HideLabel
        self.LabelVisibiliterPrime()
        self.changeConsole()
        
    
    ###########
    # METHODE #
    ###########
    def HideLabel(self) -> None:
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

    def LabelVisibiliterPrime(self) -> None:
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
        
    def LabelVisibiliterArticle(self) -> None:
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

    def Erreur(self,p_code=0) -> None:
        """
        gere le message d'erreur

        :param p_code: int
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
        if p_code == 13:
            le.setText("* ID non preciser. Veuillez en ajouter un.")
        if p_code == 14:
            le.setText("* L'ID a ete modifier veuiller ne pas y retoucher")
        if p_code == 15:
            le.setText("* ID introuvable")

    def changeConsole(self) -> None:
        """
        opere l'update de l'interface
        """
        self.LabelVisibiliterPrime()
        self.textBrowserObjet.setText("")
        #changement du titre et du textBrowser
        if self.comboBoxType.currentText() == "Article":
            #affichage des article
            self.labelTitle.setText("Liste des Articles:")
            MAJInventaire()
            for index in Global["INVENTAIRE"]:
                self.textBrowserObjet.append(str(index))       
        elif self.comboBoxType.currentText() == "Utilisateur":
            #affichage des utilisateur
            self.labelTitle.setText("Liste des Utilisateur:")
            LstUser = MAJUtilisateur()
            for index in LstUser:
                self.textBrowserObjet.append(index.__str__())
        elif self.comboBoxType.currentText() == "Facture":
            #affichage des atricle
            self.labelTitle.setText("Liste des Factures:")
            MAJFacture()
            for index in Global["FACTURE"]:
                self.textBrowserObjet.append()
    
    def clearLine(self) -> None:
        """
        Efface les line edit et autre
        """
        self.lineEditID.setText("")
        self.lineEdit1.setText("")
        self.lineEdit2.setText("")
        self.lineEdit3.setText("")
        self.lineEdit5.setText("")
        self.textEdit6.setText("")
        self.textEdit7.setText("")

    ######################
    # Bouton et ComboBox #
    ######################
    def on_comboBoxType_currentTextChanged(self):
        """
        Change le type d'object afficher et affecter par les boutons
        """
        self.changeConsole()
 
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
            Art.Serialiser(Art.__dict__(),True)
            MAJInventaire()
            self.changeConsole()
            self.clearLine()

    @pyqtSlot()
    def on_buttonModifier_clicked(self):
        """
        Modifier un produit
        """
        #recuperer les donnees
        d0 = self.lineEditID.text()
        d1 = self.lineEdit1.text()
        d2 = self.lineEdit2.text()
        d3 = self.lineEdit3.text()
        d4 = self.comboBox4.currentText()
        d5 = self.lineEdit5.text()
        d6 = self.textEdit6.toPlainText()
        d7 = self.textEdit7.toPlainText()

        #regrouper les donnees
        lstD = [d0,d1,d2,d3,d4,d5,d6,d7]

        #voir si l'id existe ou est present
        if d0 == "":
            self.Erreur(13)
        elif IDLstArticle(d0) == True:
            self.Erreur(4)
        else:#aucun erreur sur l'id on peut modifier
            modif = True
            #si un entre est vide les remplire automatiquement
            for index in range(0,5,1):
                if lstD[index] == "":
                    #bloque le fait de modifier pour juste importer les donnees
                    modif = False

                    #recuperer l'article
                    for index2 in Global["INVENTAIRE"]:
                        if d0 == index2.ArticleID:
                            Art = index2
                            break
                    
                    #remplir les line edit et autre
                    self.lineEdit1.setText(Art.str(ArticleName))
                    self.lineEdit2.setText(Art.str(Quantite))
                    self.lineEdit3.setText(Art.str(Prix))

                    #remplir la label qu'il doivent etre modifier
                    if d4 == "Pierre Magique":
                        self.lineEdit1.setText(Art.str(EnergiePierre))
                    elif d4 == "Potion":
                        self.lineEdit5.setText(Art.str(DureePotion))
                        self.textEdit6.setText(Art.str(EffetPotion))
                    else:
                        self.lineEdit5.setText(Art.str(EnergieNecessaire))
                        self.textEdit6.setText(Art.str(EffetSortillege))
                        self.textEdit7.setText(Art.str(SacrificeNecessaire))
            
            #si les entrer son presente
            if modif == True:
                #### Copier depuis on_buttonAjouter_clicked
                #reset erreur
                self.labelErreur.hide()

                #voir si l'ID est inchanger valide
                if d0 != self.lineEditID.text():
                    self.Erreur(14)
                    self.lineEditID.setText(d0)
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
                    self.changeConsole()
                    self.clearLine()

    @pyqtSlot()
    def on_buttonSupprimer_clicked(self):
        """
        Supprimer un client ou un article
        """
        #reset Erreur
        self.labelErreur.hide()

        #supprimer un client
        if self.comboBoxType.currentText() == "Utilisateur":
            #recuperer les donnees
            LstUser = MAJUtilisateur()
            IDentifiant = self.lineEditID.text()

            #detecter le client
            ClientDetected = False
            for index in LstUser:
                if index.Identifiant == IDentifiant:
                    ClientDetected = True
                    break
            
            #supprimer le client
            if ClientDetected == False:
                self.Erreur(15)
            else:
                #supprimer le fichier de sauvegarde
                os.remove(f"DATACENTER/User/{IDentifiant}.json")
                
                #supprimer le client de la liste des clients
                for index in LstUser:
                    if index.Identifiant == IDentifiant:
                        LstUser.remove(index)
                        break
                #supprimer le raccourci
                ##reset le fichier a 0
                tf = open("DATACENTER/User/raccourci.txt", "w")
                tf.write("")
                
                ##creer la chaine a raccourci
                Chaine = ""
                for index in LstUser:
                    Chaine += f"{index.Identifiant}\n"
                tf.write(Chaine)
                tf.close
        #supprimer un article
        else:
            #recuperer les donnees
            LstArticle = MajArticleLst()
            IDentifiant = self.lineEditID.text()

            #trouver l'id
            for index in LstArticle:
                if index == IDentifiant:
                    #supprimer l'id
                    LstArticle.remove(index)

                    #refaire la liste des raccourcis
                    chaine = ""
                    for index2 in LstArticle:
                        chaine += f"{index2}/n"
                        tf = open("DATACENTER/Article/raccourci.txt","w")
                        tf.write(chaine)
                        tf.close()
                #update de l'interface
                MAJInventaire()
                break


        #update interface
        self.changeConsole()
