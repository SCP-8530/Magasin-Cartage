###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe Potion
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
class Potion(Article):
    """
    classe enfant de la classe Article
    """
    def __init__(
            self,
            p_articleName = "",
            p_articleID = "",
            p_quantite = 0,
            p_prix = 0.00,
            p_effetPotion = "",
            p_dureePotion = ""
            ):
        Article.__init__(self,p_articleName,p_articleID,p_quantite,p_prix,"Potion")
        self._effetPotion = p_effetPotion
        self._dureePotion = p_dureePotion
    
    ###########
    # GET/SET #
    ###########    
    def _get_EffetPotion(self):
        return self._effetPotion
    def _set_EffetPotion(self, p_EffetPotion):
        self._effetPotion = p_EffetPotion
    EffetPotion = property(_get_EffetPotion, _set_EffetPotion)    
    
    def _get_DureePotion(self):
        return self._dureePotion
    def _set_DureePotion(self, p_DureePotion):
        if len(p_DureePotion) <= 17:
            self._dureePotion = p_DureePotion
    DureePotion = property(_get_DureePotion, _set_DureePotion)

    #################
    # Autre Methode #
    #################
    def __str__(self):
        # separation de la description en plusieur lignes de 25 caractere
        lstDescription = self._effetPotion.split()
        # calcule de ligne de 25 caractere
        strTemp1 = ""
        strTemp2 = ""
        strFinal = f"║{'Description:':<25}║"
        while True:
            #terminer la boucle si il n'y a plus rien
            if len(lstDescription) == 0:
                strFinal += f"\n║{strTemp2:^25}║"
                break
            
            #analyse
            strTemp1 += f"{lstDescription[0]} "
            if len(strTemp1) <= 25:
                strTemp2 = strTemp1
                del lstDescription[0]
            else: #creation de la chaine qui sera mis dans strChaine (voir en bas)
                strFinal += f"\n║{strTemp2:<25}║"
                strTemp1 = ""
                strTemp2 = ""

        # creation de la chaine
        strChaine = f"\n╔{'═'*25}╗"
        strChaine += f"\n║{self._articleName:^25}║"
        strChaine += f"\n╠{'═'*25}╣"
        strChaine += f"{strFinal}"
        strChaine += f"\n║{'Durée: '+self._dureePotion:<25}║"
        strChaine += f"\n╠{'═'*25}╣"
        strChaine += f"\n║{'ID: '+self._articleID:<25}║"
        strChaine += f"\n║{'Quantite: '+str(self._quantite):<25}║"
        strChaine += f"\n║{'Prix: '+str(self._prix)+'φ/unité':<25}║"
        strChaine += f"\n╚{'═'*25}╝"

        #return
        return strChaine

    def __dict__(self): 
        Dictio = {
            "Nom": self._articleName,
            "ArticleID": self._articleID,
            "Quantite":self._quantite,
            "Prix": self._prix,
            "Type": self.Type,
            "Effet Potion": self._effetPotion,
            "Duree Potion": self._dureePotion
        }

        return Dictio