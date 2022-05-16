###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Fichier qui gere les valeurs Global et les fonctions de ses valeurs
###########################################################################

#################
### PROGRAMME ###
#################
from CLASSE import Client
import json

Global = {"ID" : " ",
    "CLIENT" : Client.Client(),
    "ADMIN" : ["CR2429"],
    "INVENTAIRE" : [],
    "FACTURE" : []
    }

def RACCOURCIS():
    """
    Prepare la liste de tout les identifiant sauvegarder
    """
    tf = open("DATACENTER/User/raccourci.txt", "r")
    r = tf.read().splitlines()
    tf.close

    return r

def fCLIENT(p_identifiant):
    """
    generer un client sauvegarder
    """
    #recuperer la sauvegarde
    tf = open(f"DATACENTER/User/{p_identifiant}.json")
    dictSave = json.load(tf, object_hook=dict)
    tf.close

    #ajouter les caracteristique du client a la valeur GLOBAL
    Global["CLIENT"].Prenom = dictSave["Prenom"]
    Global["CLIENT"].Identifiant = dictSave["Identifiant"]
    Global["CLIENT"].MDP = dictSave["MDP"]
    Global["CLIENT"].Credit = str(dictSave["Credit"])
    Global["CLIENT"].LstFacture = dictSave["LstFacture"]