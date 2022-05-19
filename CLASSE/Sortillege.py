###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe Sortillege
###########################################################################

###################
### IMPORTATION ###
###################
from CLASSE.Article import Article

##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################

#################
### PROGRAMME ###
#################
class Sortillege(Article):
    """
    classe enfant de la classe Article
    
    :param p_articleName: str
    :param p_articleID: str
    :param p_quantite: int
    :param p_prix: float
    :param p_effetSortillege: str
    :param p_energieNecessaire: str
    :param p_sacrificeNecessaire: str
    """
    def __init__(
            self,
            p_articleName = "",
            p_articleID = "",
            p_quantite = 0,
            p_prix = 0.00,
            p_effetSortillege = "",
            p_energieNecessaire = "",
            p_sacrificeNecessaire = ""
            ):
        Article.__init__(self,p_articleName,p_articleID,p_quantite,p_prix,"Sortillege")
        self._effetSortillege = p_effetSortillege
        self._energieNecessaire = p_energieNecessaire
        self._sacrificeNecessaire = p_sacrificeNecessaire
    
    ###########
    # GET/SET #
    ###########    
    def _get_EffetSortillege(self):
        return self._effetSortillege
    def _set_EffetSortillege(self, p_EffetSortillege):
        self._effetSortillege = p_EffetSortillege
    EffetSortillege = property(_get_EffetSortillege, _set_EffetSortillege)    
    
    def _get_EnergieNecessaire(self):
        return self._energieNecessaire
    def _set_EnergieNecessaire(self, p_EnergieNecessaire):
        self._energieNecessaire = p_EnergieNecessaire
    EnergieNecessaire = property(_get_EnergieNecessaire, _set_EnergieNecessaire)

    def _get_SacrificeNecessaire(self):
        return self._sacrificeNecessaire
    def _set_SacrificeNecessaire(self, p_SacrificeNecessaire):
        self._sacrificeNecessaire = p_SacrificeNecessaire
    SacrificeNecessaire = property(_get_SacrificeNecessaire, _set_SacrificeNecessaire)

    #################
    # Autre Methode #
    #################
    def __str__(self) -> str:
        # separation de la description des effet en plusieur lignes de 25 caractere
        lstDescription = self._effetSortillege.split()
        # calcule de ligne de 25 caractere
        strTemp1a = ""
        strTemp2a = ""
        strFinalA = f"║{'Description:':<25}║"
        while True:
            #terminer la boucle si il n'y a plus rien
            if len(lstDescription) == 0:
                strFinalA += f"\n║{strTemp2a:^25}║"
                break
            
            #analyse
            strTemp1a += f"{lstDescription[0]} "
            if len(strTemp1a) <= 25:
                strTemp2a = strTemp1a
                del lstDescription[0]
            else: #creation de la chaine qui sera mis dans strChaine (voir en bas)
                strFinalA += f"\n║{strTemp2a:<25}║"
                strTemp1a = ""
                strTemp2a = ""

        # separation de la description des ingredients/sacrifices en plusieur lignes de 25 caractere
        lstSacrifice = self._sacrificeNecessaire.split()
        # calcule de ligne de 25 caractere
        strTemp1b = ""
        strTemp2b = ""
        strFinalB = f"║{'Description:':<25}║"
        while True:
            #terminer la boucle si il n'y a plus rien
            if len(lstSacrifice) == 0:
                strFinalB += f"\n║{strTemp2b:^25}║"
                break
            
            #analyse
            strTemp1b += f"{lstSacrifice[0]} "
            if len(strTemp1b) <= 25:
                strTemp2b = strTemp1b
                del lstSacrifice[0]
            else: #creation de la chaine qui sera mis dans strChaine (voir en bas)
                strFinalB += f"\n║{strTemp2b:<25}║"
                strTemp1b = ""
                strTemp2b = ""

        # creation de la chaine
        strChaine = f"\n╔{'═'*25}╗"
        strChaine += f"\n║{self._articleName:^25}║"
        strChaine += f"\n╠{'═'*25}╣"
        strChaine += f"{strFinalA}"
        strChaine += f"{strFinalB}"
        strChaine += f"\n║{'Énergie: '+self._energieNecessaire:<25}║"
        strChaine += f"\n╠{'═'*25}╣"
        strChaine += f"\n║{'ID: '+self._articleID:<25}║"
        strChaine += f"\n║{'Quantite: '+str(self._quantite):<25}║"
        strChaine += f"\n║{'Prix: '+str(self._prix)+'φ/unité':<25}║"
        strChaine += f"\n╚{'═'*25}╝"

        #return
        return strChaine

    def __dict__(self) -> dict: 
        Dictio = {
            "Nom": self._articleName,
            "ArticleID": self._articleID,
            "Quantite":self._quantite,
            "Prix": self._prix,
            "Type": self.Type,
            "Effet Sortillege": self._effetSortillege,
            "Energie Necessaire": self._energieNecessaire,
            "Sacrifice Necessaire": self._sacrificeNecessaire
        }

        return Dictio
