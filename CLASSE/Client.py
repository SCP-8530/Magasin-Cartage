###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Classe Client
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
class Client:
    """
    Classe qui gere le compte des clients

    :param p_prenom: str
    :param p_identifiant: str
    :param p_mdp: str
    :param p_credit: float
    :param p_LstFacture: list
    """
    def __init__(
            self,
            p_prenom = "",
            p_identifiant = "",
            p_mdp = "",
            p_credit = 0.0,
            p_LstFacture = []
            ):
            self._prenom = p_prenom
            self._identifiant = p_identifiant
            self._mdp = p_mdp
            self._credit = p_credit
            self.LstFacture = p_LstFacture

    ###########
    # GET/SET #
    ###########
    def _get_Prenom(self):
        return self._prenom
    def _set_Prenom(self, p_Prenom):
        if len(p_Prenom) <= 25 and p_Prenom.isalpha() == True:
            self._prenom = p_Prenom
    Prenom = property(_get_Prenom,_set_Prenom)

    def _get_Identifiant(self):
        return self._identifiant
    def _set_Identifiant(self, p_Identifiant):
        #exemple d'identifiant CR2429
        if len(p_Identifiant) == 6:
            if p_Identifiant[:2] in ["CR","ET","FC"]:
                if p_Identifiant[3:6].isnumeric() == True:
                    self._identifiant = p_Identifiant
    Identifiant = property(_get_Identifiant,_set_Identifiant)
    
    def _get_MDP(self):
        return self._mdp
    def _set_MDP(self, p_MDP):
        #verifie qu'il y a au moins une minuscule, une majuscule et un chiffre
        critere = []
        for valeur in p_MDP:
            if valeur.isnumeric() == True:
                critere.append(1)
            if valeur.isalpha() == True:
                if str(valeur).isupper() == True:
                    critere.append(2)
                if valeur.islower() == True:
                    critere.append(3)
        #si tout les critere son respecter enregistre le MDP
        if critere.count(1) > 0:
            if critere.count(2) > 0:
                if critere.count(3) > 0:
                    self._mdp = p_MDP

    MDP = property(_get_MDP,_set_MDP)

    def _get_Credit(self):
        return self._credit
    def _set_Credit(self, p_Credit):
        if p_Credit.isdecimal() == True or p_Credit.isnumeric():
            self._credit = float(p_Credit)
    Credit = property(_get_Credit,_set_Credit)
    
    #################
    # Autre Methode #
    #################

    def __dict__(self) -> dict:
        """
        creation d'un dictionnaire des informations du client
        """
        DictSave = {
            "Prenom":self._prenom,
            "Identifiant":self._identifiant,
            "MDP":self._mdp,
            "Credit":self._credit,
            "LstFacture":self.LstFacture,
        }

        return DictSave
    
    def __str__(self) -> str:
        """
        Creation d'un string
        """
        StrChaine = f"\n**********"
        StrChaine +=f"\n* Prenom: {self._prenom}"
        StrChaine +=f"\n* Identifiant: {self._identifiant}"
        StrChaine +=f"\n* MDP: {self._mdp}"
        StrChaine +=f"\n* Credit: {self._credit}"
        StrChaine +=f"\n* LstFacture: {self.LstFacture}"
        StrChaine += "\n**********"

        return StrChaine

    def Serialisation(self,New=False) -> None:
        """
        Creation d'un fichier pour serialiser le client

        :param New: bool
        """
        #creation du fichier
        tf = open(f"DATACENTER/User/{self._identifiant}.json","w")
        json.dump(self.__dict__(),tf,indent=4,sort_keys=True)
        tf.close()
        
        #ajout du raccourci si c'est un nouveau client qui vient d'etre creer
        if New == True:
            tf = open(f"DATACENTER/User/raccourci.txt", "a")
            tf.write(f"\n{self._identifiant}")
            tf.close()

    def Payer(self,p_Cout=0.00) -> None:
        """
        Paye une facture

        :param p_Cout: float
        """
        #paye la facture
        self._credit -= p_Cout
        self.Serialisation()