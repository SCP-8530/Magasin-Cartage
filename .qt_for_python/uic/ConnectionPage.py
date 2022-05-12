# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConnectionPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(359, 243)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 190, 341, 41))
        self.BoiteABouton = QHBoxLayout(self.horizontalLayoutWidget)
        self.BoiteABouton.setObjectName(u"BoiteABouton")
        self.BoiteABouton.setContentsMargins(0, 0, 0, 0)
        self.buttonConnection = QPushButton(self.horizontalLayoutWidget)
        self.buttonConnection.setObjectName(u"buttonConnection")

        self.BoiteABouton.addWidget(self.buttonConnection)

        self.buttonNouveauCompte = QPushButton(self.horizontalLayoutWidget)
        self.buttonNouveauCompte.setObjectName(u"buttonNouveauCompte")

        self.BoiteABouton.addWidget(self.buttonNouveauCompte)

        self.labelIdentifiant = QLabel(Dialog)
        self.labelIdentifiant.setObjectName(u"labelIdentifiant")
        self.labelIdentifiant.setGeometry(QRect(70, 30, 199, 41))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(18)
        self.labelIdentifiant.setFont(font)
        self.labelMotDePasse = QLabel(Dialog)
        self.labelMotDePasse.setObjectName(u"labelMotDePasse")
        self.labelMotDePasse.setGeometry(QRect(70, 100, 199, 41))
        self.labelMotDePasse.setFont(font)
        self.lineEditIdentifiant = QLineEdit(Dialog)
        self.lineEditIdentifiant.setObjectName(u"lineEditIdentifiant")
        self.lineEditIdentifiant.setGeometry(QRect(70, 70, 201, 31))
        self.lineEditMotDePasse = QLineEdit(Dialog)
        self.lineEditMotDePasse.setObjectName(u"lineEditMotDePasse")
        self.lineEditMotDePasse.setGeometry(QRect(70, 140, 201, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.buttonConnection.setText(QCoreApplication.translate("Dialog", u"Se connecter", None))
        self.buttonNouveauCompte.setText(QCoreApplication.translate("Dialog", u"Cr\u00e9er un nouveau compte", None))
        self.labelIdentifiant.setText(QCoreApplication.translate("Dialog", u"Identifiant :", None))
        self.labelMotDePasse.setText(QCoreApplication.translate("Dialog", u"Mot de passe :", None))
    # retranslateUi

