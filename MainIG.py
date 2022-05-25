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
import random
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import datetime


#interface garphique
import INTERFACEGRAPHIQUE.PY.MainPage as MainPage
import ConnectionPageIG
import AdminIG
import AjoutCreditIG
import FactureIG


#autre
import CLASSE.Facture as F
import CLASSE.Article as A
import CLASSE.PierreMagique as PM
import CLASSE.Potion as P
import CLASSE.Sortillege as S
import GLOBAL as G
from main import MAJInventaire
##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################
Panier = F.Facture()

###############################
### DECLARATION DE FONCTION ###
###############################
def OuvrirConnectionPage() -> None:
    """
    gere la connection
    """
    while True:
        if G.Global["ID"]=="":
            form = ConnectionPageIG.gui()
            form.show()
            form.exec_()
        else:
            break

def ProduitSelect(p_ID="") -> object:
    """
    recupere un produit dans l'inventaire

    :param p_ID: str
    """
    for index in G.Global["INVENTAIRE"]:
        if index.ArticleID == p_ID:
            return index

def IndexInventaire(p_ID="") -> int:
    """
    Recuperer l'index ou se trouve un article dans l'inventaire

    :param p_ID: str
    """
    for index in range(0,len(G.Global["INVENTAIRE"]),1):
        if G.Global["INVENTAIRE"][index].ArticleID == p_ID:
            return index

def OuvrirAdminIG() -> None:
    """
    Gere l'ouverture de la page admin
    """
    form = AdminIG.gui()
    form.show()
    form.exec_()

def ConfigPanier() -> None:
    """
    Configure le Panier
    """
    str1 = G.Global["ID"]
    str2_1 = datetime.datetime.today()
    str2_2 = str2_1.strftime("%d%m%y")
    str3 = str(random.randint(0,1000))
    Panier.Date = str2_1.strftime("%d %B %Y")
    Panier.Numero = f"{str1}{str2_2}{str3}"
    Panier.LstArticle = []

def OuvrirCredit() -> None:
    G.Global["DIALOG ACTIF"] = True
    form = AjoutCreditIG.gui()
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
        self.setWindowTitle("Page principal")
        self.labelErreur.hide()
        OuvrirConnectionPage()
        MAJInventaire()
        self.Filtrage()
        ConfigPanier()
        self.updateCredit()
    
    ###########
    # METHODE #
    ###########
    def MAJPanier(self) -> None:
        """
        Update le Panier
        """
        self.textBrowserPanier.setText(Panier.__str__())

    def Filtrage(self) -> None:
        #simplfication de valeur
        filtre = self.comboBoxFiltre.currentText()
        console = self.textBrowserInventaire

        #reset de la liste des article
        console.setText("")

        #filtrage
        for index in G.Global["INVENTAIRE"]:
            if filtre == "Tous type de produit": #pas de filtre
                console.append(str(index))
            if filtre == index.Type: #il y a un filtre
                console.append(str(index))

    def Erreur(self,p_code=0) -> None:
        """
        Fonction qui gere les erreurs

        :param p_code: int
        """
        #raccourci
        le = self.labelErreur
        le.show()
        if p_code == 1:
            le.setText("* L'ID n'existe pas")
        if p_code == 2:
            le.setText("* La quantite n'est pas valide")
        if p_code == 3:
            le.setText("* La quantite est trop élevé")
        if p_code == 4:
            le.setText("* Vous n'avez pas assez de credit pour vos achats")
    
    def updateCredit(self) -> None:
        """
        Affiche le nombre de credit que l'on possede
        """
        nombre = G.Global["CLIENT"].Credit
        self.buttonCredit.setText(f"Credit: {nombre:.2f}φ")
    ####################
    # Bouton et Combox #
    ####################
    def on_comboBoxFiltre_currentTextChanged(self):
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
        tf = open("DATACENTER/Article/raccourci.txt", "r")
        r = tf.read().splitlines()
        tf.close
        
        #ouvre la page admin
        if IdProduit == "Admin" or QuantiterProduit == "Admin":
            if G.Global["ADMIN"].count(G.Global["ID"]) == 1:
                OuvrirAdminIG()
                self.lineEditID.setText("")
                self.lineEditQuantite.setText("")
        else: #ajoute un produit au panier
            #l'id n'existe pas
            if r.count(IdProduit) == 0:
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
                #clean line edit
                self.lineEditID.setText("")
                self.lineEditQuantite.setText("")

                #modifier ou ajouter
                modifier = False
                for index in Panier.LstArticle:
                    if IdProduit == index.ArticleID:
                        modifier = True
                        break
                    

                if modifier == False:
                    indexe = IndexInventaire(IdProduit)
                    ProduitPanier = G.Global["INVENTAIRE"][indexe]
                    ProduitPanier.Quantite = QuantiterProduit
                    #deplacer de l'inventaire au panier
                    Panier.LstArticle.append(ProduitPanier)
                    self.MAJPanier()
                elif modifier == True:
                    #ajouter un produit du panier
                    for index in Panier.LstArticle:
                        if index.ArticleID == IdProduit:
                            int1 = index.Quantite
                            int2 = int(QuantiterProduit)
                            int3 =  int2 + int1
                            #verifier que la nouvelle qunatite ne depasse pas l'inventaire
                            if int3 > int(ProduitSelect(IdProduit).Quantite):
                                self.Erreur(3)
                            elif int3 <= ProduitSelect(IdProduit).Quantite:
                                index.Quantite = str(int3)
                                self.MAJPanier()
                            break
                
    @pyqtSlot()
    def on_buttonRetirer_clicked(self):
        """
        retire un element du panier
        """
        #reset des erreurs
        self.labelErreur.hide()

        #recuperer les informations
        IdProduit = self.lineEditID.text()
        QuantiterProduit = self.lineEditQuantite.text()

        #verifier si l'element est dans le panier
        for index in Panier.LstArticle:
            if index.ArticleID == IdProduit:
                self.labelErreur.hide()
                #verifier que la quantier est valide
                try:
                    int(QuantiterProduit)
                except ValueError:
                    self.Error(2)
                else:
                    #verifier que la quantiter est pas trop grande
                    if index.Quantite < int(QuantiterProduit):
                        self.Erreur(3)
                break
            else:
                self.Erreur(1)
        
        #Retire le produit du panier
        if self.labelErreur.isVisible() == False:
            #clean line edit
            self.lineEditID.setText("")
            self.lineEditQuantite.setText("")
            
            #retrouver l'article a modifier
            for index in range(0,len(Panier.LstArticle),1):
                if Panier.LstArticle[index].ArticleID == IdProduit:
                    int1 = Panier.LstArticle[index].Quantite
                    int2 = int(QuantiterProduit)
                    int3 = int1 - int2
                    Panier.LstArticle[index].Quantite = str(int3)
        
        #mettre a jour l'interface
        self.MAJPanier()

    @pyqtSlot()
    def on_buttonCredit_clicked(self):
        """
        Ajout des credit au client
        """
        #ouverture de la fenetre
        OuvrirCredit()

        #sauvegarde
        self.updateCredit()
        G.Global["CLIENT"].Serialisation()

    @pyqtSlot()
    def on_buttonFacture_clicked(self):
        """
        Ouvre l'historique des factures
        """
        form = FactureIG.gui()
        form.show()
        form.exec_()

    @pyqtSlot()
    def on_buttonPayer_clicked(self,p_panier = Panier):
        """
        Payer se qui se trouve dans le panier
        """
        #mettre le client dans le panier
        p_panier.Client = G.Global["CLIENT"]

        #payer
        if p_panier.PayerFacture() == True:    
            #mise a jour de l'inventaire
            for index in p_panier.LstArticle:
                #trouver l'id du produit a modif
                IdDuProduitAModif = index.ArticleID

                #recuperer l'objet a modifier se trouvant dans la liste
                for index2 in range(0,len(G.Global["INVENTAIRE"]),1):
                    indexDansGlobal = G.Global["INVENTAIRE"][index2].ArticleID
                    if indexDansGlobal == IdDuProduitAModif:
                        #modif la serialisation
                        tf = open(f"DATACENTER/Article/{IdDuProduitAModif}.json","r")
                        aModif = json.load(tf,object_hook=dict)
                        tf.close
                        aModif["Quantite"] = aModif["Quantite"] - index.Quantite
                        
                        #mettre a jour la serialisation/(recreer le produit parce que pourquoi pas)
                        if aModif["Type"] == "Pierre Magique":
                            Art = PM.PierreMagique()
                            Art.Type = aModif["Type"]
                            Art.EnergiePierre = aModif["Energie Pierre"]
                        elif aModif["Type"] == "Potion":
                            Art = P.Potion()
                            Art.Type = aModif["Type"]
                            Art.EffetPotion = aModif["Effet Potion"]
                            Art.DureePotion = aModif["Duree Potion"]
                        else:
                            Art = S.Sortillege()
                            Art.Type = aModif["Type"]
                            Art.EffetSortillege = aModif["Effet Sortillege"]
                            Art.EnergieNecessaire = aModif["Energie Necessaire"]
                            Art.SacrificeNecessaire = aModif["Sacrifice Necessaire"]
                        Art.ArticleID = aModif["ArticleID"]
                        Art.ArticleName = aModif["Nom"]
                        Art.Prix = str(aModif["Prix"])
                        Art.Quantite = str(aModif["Quantite"])
                        Art.Serialiser(p_dict=Art.__dict__())
                        break

                
                #modification a faire
                MAJInventaire()

                
            #reset du panier
            ConfigPanier()
            
            #update interface
            self.textBrowserPanier.setText("")
            self.labelErreur.setText("Merci pour votre achat")

        else: #pas assez d'argent
            self.Erreur(4)

    
