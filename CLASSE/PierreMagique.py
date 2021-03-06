###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe Pierre Magique
###########################################################################

###################
### IMPORTATION ###
###################
import CLASSE.Article as A

##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################

#################
### PROGRAMME ###
#################
class PierreMagique(A.Article):
    """
    classe enfant de la classe Article

    :param p_articleName: str
    :param p_articleID: str
    :param p_quantite: int
    :param p_prix: float
    :param p_energiePierre: str
    """
    def __init__(
            self,
            p_articleName = "",
            p_articleID = "",
            p_quantite = 0,
            p_prix = 0.00,
            p_energiePierre = ""
            ):
        A.Article.__init__(self,p_articleName,p_articleID,p_quantite,p_prix,"Pierre Magique")
        self._energiePierre = p_energiePierre
    
    ###########
    # GET/SET #
    ###########        
    def _get_EnergiePierre(self):
        return self._energiePierre
    def _set_EnergiePierre(self, p_EnergiePierre):
        if len(p_EnergiePierre) <= 17:
            self._energiePierre = p_EnergiePierre
    EnergiePierre = property(_get_EnergiePierre, _set_EnergiePierre)

    #################
    # Autre Methode #
    #################
    def __str__(self) -> str:
        # creation de la chaine
        strChaine = f"\n╔{'═'*25}╗"
        strChaine += f"\n║{self._articleName:^25}║"
        strChaine += f"\n╠{'═'*25}╣"
        strChaine += f"\n║{'Énergie: '+self._energiePierre:<25}║"
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
            "Energie Pierre": self._energiePierre
        }

        return Dictio