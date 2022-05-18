###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe Article
###########################################################################

###################
### IMPORTATION ###
###################
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
class Article:
    """
    classe parent gerant les differents articles du magasins et des factures 
    """
    def __init__(self, p_articleName="", p_articleID="", p_quantite=0, p_prix=0.00, p_type=""):
        self._articleName = p_articleName
        self._articleID = p_articleID
        self._quantite = p_quantite
        self._prix = p_prix
        self.Type = p_type
    
    ###########
    # GET/SET #
    ###########
    def _get_ArticleName(self):
        return self._articleName
    def _set_ArticleName(self, p_ArticleName):
        if len(p_ArticleName) <= 25:
            self._articleName = p_ArticleName
    ArticleName = property(_get_ArticleName, _set_ArticleName)
    
    def _get_ArticleID(self):
        return self._articleID
    def _set_ArticleID(self, p_ArticleID):
        if len(p_ArticleID) == 4 and p_ArticleID.isnumeric() == True:
            self._articleID = p_ArticleID
    ArticleID = property(_get_ArticleID, _set_ArticleID)
    
    def _get_Quantite(self):
        return self._quantite
    def _set_Quantite(self, p_Quantite=""):
        if p_Quantite.isnumeric() == True:
            self._quantite = int(p_Quantite)
    Quantite = property(_get_Quantite, _set_Quantite)
    
    def _get_Prix(self):
        return self._prix
    def _set_Prix(self, p_Prix):
        if p_Prix.isdecimal() == True or p_Prix.isnumeric == True:
            if float(p_Prix) > 0:
                self._prix = float(p_Prix)
    Prix = property(_get_Prix,_set_Prix)

    #################
    # Autre Methode #
    #################
    def PrixTotal(self):
        """
        Calcule prix total a debourser celon cela la quantiter de que l'on a
        """
        intPrix = self._prix * self._quantite
        return intPrix

    def __str__(self):
        strChaine = "*"*25
        strChaine += f"\n* Nom de l'article: {self._articleName}"
        strChaine += f"\n* Numero de l'article: {self._articleID}"
        strChaine += f"\n* Quantite: {self._quantite}"
        strChaine += f"\n* Prix a l'unité: {self._prix}"
        strChaine += f"\n* Prix de l'ensemble: {self.PrixTotal()}"
        strChaine += f"\n"+"*"*25

    def Serialiser(self,p_dict):
        """
        Gere la serialisation des articles
        """
        tf = open(f"DATACENTER/Article/{self._articleID}.json","w")
        json.dump(p_dict,tf,indent=4,sort_keys=True)
        tf.close
