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
    """
    def __init__(
            self,
            p_prenom = "",
            p_identifiant = "",
            p_mdp = "",
            p_credit = 0.00,
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
        if len(p_Prenom) <= 25:
            self._prenom = p_Prenom
    Prenom = property(_get_Prenom(),_set_Prenom())

    def _get_Identifiant(self):
        return self._prenom
    def _set_Identifiant(self, p_Identifiant):
        if len(p_Identifiant) == 6:
            self._identifiant = p_Identifiant
    Identifiant = property(_get_Identifiant(),_set_Identifiant())
    
    def _get_MDP(self):
        return self._mdp
    def _set_MDP(self, p_MDP):
        self._mdp = p_MDP
    MDP = property(_get_MDP(),_set_MDP())

    def _get_Credit(self):
        return self._credit
    def _set_Credit(self, p_Credit):
        if p_Credit.isdecimal == True:
            self._credit = float(p_Credit)
    Credit = property(_get_Credit(),_set_Credit())
    
    #################
    # Autre Methode #
    #################

    def __dict__(self):
        """
        creation d'un dictionnaire des informations du client
        """
        DictSave = {
            ["Prenom"]:self._prenom,
            ["Identifiant"]:self._identifiant,
            ["MDP"]:self._mdp,
            ["Credit"]:self._credit,
            ["LstFacture"]:self.LstFacture,
        }

        return DictSave
    
    def __str__(self):
        """
        Creation d'un string
        """
        StrChaine = "**********"
        StrChaine +=f"* Prenom: {self._prenom}"
        StrChaine +=f"* Identifiant: {self._identifiant}"
        StrChaine +=f"* MDP: {self._mdp}"
        StrChaine +=f"* Credit: {self._credit}"
        StrChaine +=f"* LstFacture: {self.LstFacture}"
        StrChaine += "**********"

        return StrChaine

    def Serialisation(self,New=False):
        """
        Creation d'un fichier pour serialiser le client
        """
        #creation du fichier
        tf = open(f"DATACENTER/User/{self._identifiant}.json","w")
        json.dump(self.__dict__(),tf,indent=4,sort_keys=True)
        tf.close()
        
        #ajout du raccourci si c'est un nouveau client qui vient d'etre creer
        if New == True:
            tf = open(f"DATACENTER/Factures/raccourci.txt", "a")
            tf.write(f"{self._identifiant}\n")
            tf.close()

    def Payer(self,p_Cout):
        """
        Paye une facture
        """
        #paye la facture
        self._credit -= p_Cout
        self.Serialisation()