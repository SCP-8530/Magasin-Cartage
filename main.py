###########################################################################
### 420-2G2-HU - Programmation Orientée Objet
### Travail: Projet de fin de session
### Nom: Guillaume Paoli
### Numero Étudiant: 2142678
### Description du fichier: Fichier Main
###########################################################################

###################
### IMPORTATION ###
###################
from GLOBAL import *
import MainIG
import sys
from PyQt5 import QtWidgets
##########################################################
### DECLARATION DE VALEUR, DE LISTE ET DE DICTIONNAIRE ###
##########################################################

###############################
### DECLARATION DE FONCTION ###
###############################
def Main():
    """
    Ouvre la page principal du magasin
    """
    app = QtWidgets.QApplication(sys.argv)
    form = MainIG.gui()
    form.show()
    app.exec()

#################
### PROGRAMME ###
#################

#Demarrage de l'application
if __name__ == "__main__":
    Main()