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
import json
import CLASSE.Client as C
import main as M

#################
### PROGRAMME ###
#################   
class Facture:
    """
    Classe qui gere les factures des differents clients

    :param p_numero: str
    :param p_date: str
    :param p_LstArticle: lst
    :param p_Client: object
    """
    def __init__(self,p_numero = "", p_date = "", p_LstArticle = [], p_Client = C.Client()):
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
        self._numero = p_Numero
    Numero = property(_get_Numero, _set_Numero)

    def _get_Date(self):
        return self._date
    def _set_Date(self, p_Date):
        self._date = p_Date
    Date = property(_get_Date, _set_Date)

    #################
    # Autre Methode #
    #################
    def __str__(self,p_bool=False) -> str:
        """
        Creation d'un string des informations a afficher dans le labelPanier

        :param p_bool: bool
        """
        #parcourrir la liste des article pour recuperer un ligne de string
        StrArticle = ""
        pt = 0.0
        for index in self.LstArticle:
            if p_bool == False:
                nom = str(index.ArticleName)
                quantite = str(index.Quantite)
                prix = index.PrixTotal()
                pt += index.PrixTotal()
            if p_bool == True:
                nom = index["Nom"]
                quantite = index["Quantite"]
                prix = index["Prix"]
                pt += index["Prix"]

            StrArticle += f"\n║ {f'{nom} -- {quantite}':<30}{f'{prix:.2f}φ':>10} ║"
        
        #creation du string
        StrChaine = ""
        StrChaine += f"\n╔{'═'*42}╗"
        StrChaine += f"\n║ {'Numero de Facture: ':<20}{f'{self._numero}':>20} ║"
        StrChaine += f"\n║ {'Date: ':<20}{f'{self._date}':>20} ║"
        StrChaine += f"\n║ {'Cout Total:':<20}{f'{pt:.2f}φ':>20} ║"
        StrChaine += f"\n╠{'═'*42}╣"
        StrChaine += f"\n║ {'Nom -- Quantite':<25}{'Prix':>15} ║"
        StrChaine += f"{StrArticle}"
        StrChaine += f"\n╚{'═'*42}╝"

        #envoie du string
        return StrChaine

    def __dict__(self) -> dict:
        """
        creation d'un dictionnaire des informations
        """
        #simplification de lstArticle
        simpleLST = []
        for index in self.LstArticle:
            simpleLST.append(index.__dict__())
        
        #recupere un client modifier sans liste facture
        self.Client.LstFacture = []

        #creation du dict
        DictSave = {
            "Numero":self._numero,
            "Date":self._date,
            "LstArticle":simpleLST,
            "Client":self.Client.__dict__()
        }

        return DictSave

    def PrixTotal(self) -> float:
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

    def PayerFacture(self) -> bool:
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
        
    def Serialisation(self) -> None:
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

        #ajouter la facture dans les donne du client
        self.Client.LstFacture.append(self)
        self.Client.Serialisation()

    def Deserialise(self,p_dict={}) -> None:
        """
        Permet a la classe de se recreer a parti d'un dictionnaire

        :param p_dict: dict
        """
        #mettre les element classique
        self._numero = p_dict["Numero"]
        self._date = p_dict["Date"]
        self.LstArticle = p_dict["LstArticle"]
        
        #instancier correctement le client
        self.Client = M.InstancieClient(p_dict["Client"])
