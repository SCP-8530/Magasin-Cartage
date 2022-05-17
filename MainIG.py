###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe MainIG
###########################################################################

###################
### IMPORTATION ###
###################
#module python
import json
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

#interface garphique
import INTERFACEGRAPHIQUE.PY.MainPage as MainPage
import ConnectionPageIG
import AdminIG

#article
from CLASSE.Potion import Potion
from CLASSE.PierreMagique import PierreMagique
from CLASSE.Sortillege import Sortillege

#autre
from CLASSE.Facture import Facture
from GLOBAL import Global
##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################
Panier = Facture()
###############################
### DECLARATION DE FONCTION ###
###############################
def OuvrirConnectionPage():
    """
    gere la connection
    """
    while True:
        if Global["ID"]=="":
            form = ConnectionPageIG.gui()
            form.show()
            form.exec_()
        else:
            break

def MAJInventaire():
    """
    recupere tout les produit creer pour les mettre dans l'inventaire
    """
    #recupere la liste des ID
    tf = open("DATACENTER/Article/raccourci.txt","r")
    LstArticleID = tf.read().splitlines()
    tf.close

    #instancier les different article dans l'inventaire
    for index in LstArticleID:
        #recupere la sauvegarde de l'article
        tf = open(f"DATACENTER/Article/{index}.json")
        ArticleSave = json.load(tf, object_hook=dict)
        tf.close()

        #instencie l'objet
        ##potion
        if ArticleSave["Type"] == "Potion":
            Art = Potion()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = ArticleSave["Quantite"]
            Art.Prix = ArticleSave["Prix"]
            Art.EffetPotion = ArticleSave["Effet Potion"]
            Art.DureePotion = ArticleSave["Duree Potion"]

            #mettre dans l'inventaire
            Global["INVENTAIRE"].append(Art)
        ##sortillege
        elif ArticleSave["Type"] == "Sortillege":
            Art = Sortillege()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = ArticleSave["Quantite"]
            Art.Prix = ArticleSave["Prix"]
            Art.EffetSortillege = ArticleSave["Effet Sortillege"]
            Art.EnergieNecessaire = ArticleSave["Energie Necessaire"]
            Art.SacrificeNecessaire = ArticleSave["Sacrifice Necessaire"]

            #mettre dans l'inventaire
            Global["INVENTAIRE"].append(Art)
        ##pierre magique
        elif ArticleSave["Type"] == "PierreMagique":
            Art = PierreMagique()
            Art.ArticleName = ArticleSave["Nom"]
            Art.ArticleID = ArticleSave["ArticleID"]
            Art.Quantite = ArticleSave["Quantite"]
            Art.Prix = ArticleSave["Prix"]
            Art.EnergiePierre = ArticleSave["Energie Pierre"]

            #mettre dans l'inventaire
            Global["INVENTAIRE"].append(Art)

def ProduitSelect(p_ID) -> object:
    """
    recupere un produit dans l'inventaire
    """
    for index in Global["INVENTAIRE"]:
        if index.ArticleID == p_ID:
            return index

def IndexInventaire(p_ID) -> int:
    """
    Recuperer l'index ou se trouve un article dans l'inventaire
    """
    for index in range(0,len(Global["INVENTAIRE"]),1):
        if Global["INVENTAIRE"].ArticleID == p_ID:
            return index

def OuvrirAdminIG():
    """
    Gere l'ouverture de la page admin
    """
    form = AdminIG.gui()
    form.show()
    form.exec_()

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
        MAJInventaire()
    
    ###########
    # METHODE #
    ###########
    def MAJPanier(self):
        """
        Update le Panier
        """
        self.textBrowserPanier.setText(Panier.__str__())

    def Filtrage(self):
        #simplfication de valeur
        filtre = self.comboBoxFiltre.currentText()
        console = self.textBrowserInventaire

        #reset de la liste des article
        self.textBrowserInventaire.setText("")

        #filtrage
        for index in Global["INVENTAIRE"]:
            if filtre == "Tous type de produit": #pas de filtre
                console.append(Global["INVENTAIRE"][index])
            if filtre == Global["INVENTAIRE"][index].type: #il y a un filtre
                console.append(Global["INVENTAIRE"][index])

    def Erreur(self,p_code):
        """
        Fonction qui gere les erreurs
        """
        #raccourci
        le = self.labelErreur
        if p_code == 1:
            le.setText("* L'ID n'existe pas")
        if p_code == 2:
            le.setText("* La quantite n'est pas valide")
        if p_code == 3:
            le.setText("* La quantite est trop élevé")

    ####################
    # Bouton et Combox #
    ####################
    def on_comboBoxFiltre_changed(self):
        """
        Gere le filtre des article afficher textBrowserInventaire de facon volontaire
        """
        self.Filtrage()
        
    
    @pyqtSlot()
    def on_buttonAjouter_clicked(self):
        """
        Ajouter un produit au panier

        easteregg: ouvre la page admin
        """
        #reset des erreurs
        self.labelErreur.hide()

        #recuperer les informations
        IdProduit = self.lineEditID.text()
        QuantiterProduit = self.lineEditQuantite.text()

        #ouvre la page admin
        if IdProduit == "Admin" and QuantiterProduit == "Admin":
            if Global["ADMIN"].count(Global["ID"]) == 1:
                OuvrirAdminIG()
        else: #ajoute un produit au panier
            #l'id n'existe pas
            if Global["Inventaire"].count(IdProduit) == 0:
                self.Erreur(1)
            #La quantiter n'est pas un chiffre
            elif QuantiterProduit.isnumeric == False:
                self.Erreur(2)
            #la quantiter est 0 ou moins
            elif int(QuantiterProduit) <= 0:
                self.Erreur(2)
            #la quantiter est trop elever
            elif int(QuantiterProduit) > ProduitSelect(IdProduit).Quantite:
                self.Erreur(3)
            #aucune erreur
            else:
                #configuere les objets
                ProduitInventaire = Global["INVENTAIRE"][IndexInventaire(IdProduit)]
                ProduitPanier = ProduitInventaire
                ProduitPanier.Quantite = QuantiterProduit

                #deplacer de l'invantaire au panier
                ProduitInventaire.Quantite -= QuantiterProduit
                Panier.LstArticle.append(ProduitPanier)

                #mettre a jour les interfaces
                MAJInventaire()
                self.Filtrage()
                self.MAJPanier()
