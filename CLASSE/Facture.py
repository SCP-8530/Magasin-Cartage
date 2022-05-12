###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe Facture
###########################################################################

###################
### IMPORTATION ###
###################
from Client import Client
import json

##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################

#################
### PROGRAMME ###
#################
class Facture:
    """
    Classe qui gere les factures des differents clients
    """
    def __init__(self,p_numero = "", p_date = "", p_LstArticle = [], p_Client = Client()):
        self._numero = p_numero
        self._date = p_date
        self.LstArticle = p_LstArticle
        self.Client = p_Client

    ###########
    # GET/SET #
    ###########
    def _get_Numero(self):
        return self._numero
    def _set_Numero(self, p_Numero):
        if p_Numero.isnumeric == True:
            self._numero = p_Numero
    Numero = property(_get_Numero(), _set_Numero())

    def _get_Date(self):
        return self._date
    def _set_Date(self, p_Date):
        self._date = p_Date
    Date = property(_get_Date(), _set_Date())

    #################
    # Autre Methode #
    #################
    def __str__(self) -> str:
        """
        Creation d'un string des informations a afficher dans le labelPanier
        """
        #parcourrir la liste des article pour recuperer un ligne de string
        StrArticle = ""
        for index in self.LstArticle:
            nom = self.LstArticle[index].ArticleName
            quantite = self.LstArticle[index].Quantite
            prix = self.LstArticle[index].PrixTotal()

            StrArticle += f"{f'{nom}({quantite})':<30}{f'{prix}φ':>10}"

        #creation du string
        StrChaine = ""
        StrChaine += f"\n{'*'*40}"
        StrChaine += f"\n* {'Numero de Facture: '+{self._numero}:36} *"
        StrChaine += f"\n* {'Date: '+{self._date}:36} *"
        StrChaine += f"\n* {'Cout Total:':<20}{f'{self.PrixTotal()}φ':>16} *"
        StrChaine += f"\n{'*'*40}"
        StrChaine += f"\n{'Nom(Quantite)':<25}{'Prix':>15}"
        StrChaine += f"\n{StrArticle}"

        #envoie du string
        return StrChaine

    def __dict__(self) -> dict:
        """
        creation d'un dictionnaire des informations
        """
        DictSave = {
            ["Numero"]:self._numero,
            ["Date"]:self._date,
            ["LstArticle"]:self.LstArticle,
            ["Client"]:self.Client
        }

        return DictSave

    def PrixTotal(self):
        """
        Calculer le cout total de la facture
        """
        #generation de la valeur a 0
        fltPrixTotal = 0.00

        #parcour des articles dans la liste
        for index in range(0, len(self.LstArticle), 1):
            #recuperer le payement
            fltPrixTotal += self.LstArticle[index].PrixTotal()
        
        #envoie de la valeur
        return fltPrixTotal

    def PayerFacture(self):
        """
        Assure le payement de la facture
        """
        #recuperation du cout
        cout = self.PrixTotal()

        #verifier que vous pouvez payer
        if self.Client.Credit < cout:
            return False #Pas assez de credit (φ) pour payer
        else:
            self.Client.Payer(cout)
            self.Serialisation()
            return True
        
    def Serialisation(self):
        """
        Creation d'un fichier pour serialiser la facture lorsqu'elle est payer
        """
        #creation du fichier
        tf = open(f"DATACENTER/Factures/{self._numero}.json","w")
        json.dump(self.__dict__(),tf,indent=4,sort_keys=True)
        tf.close

        #ajout du raccourci
        tf = open(f"DATACENTER/Factures/raccourci.txt", "a")
        tf.write(f"{self._numero}\n")
        tf.close()