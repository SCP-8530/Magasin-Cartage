# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewUserPage.ui'
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
        Dialog.resize(314, 480)
        self.labelTitle = QLabel(Dialog)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(0, 10, 311, 31))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitle.setFont(font)
        self.labelPrenom = QLabel(Dialog)
        self.labelPrenom.setObjectName(u"labelPrenom")
        self.labelPrenom.setGeometry(QRect(30, 50, 256, 31))
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(13)
        self.labelPrenom.setFont(font1)
        self.lineEditPrenom = QLineEdit(Dialog)
        self.lineEditPrenom.setObjectName(u"lineEditPrenom")
        self.lineEditPrenom.setGeometry(QRect(30, 80, 251, 31))
        self.labelIdentifiant = QLabel(Dialog)
        self.labelIdentifiant.setObjectName(u"labelIdentifiant")
        self.labelIdentifiant.setGeometry(QRect(30, 130, 256, 31))
        self.labelIdentifiant.setFont(font1)
        self.lineEditIdentifiant = QLineEdit(Dialog)
        self.lineEditIdentifiant.setObjectName(u"lineEditIdentifiant")
        self.lineEditIdentifiant.setGeometry(QRect(30, 160, 251, 31))
        self.labelMDP = QLabel(Dialog)
        self.labelMDP.setObjectName(u"labelMDP")
        self.labelMDP.setGeometry(QRect(30, 210, 256, 31))
        self.labelMDP.setFont(font1)
        self.lineEditMDP = QLineEdit(Dialog)
        self.lineEditMDP.setObjectName(u"lineEditMDP")
        self.lineEditMDP.setGeometry(QRect(30, 240, 251, 31))
        self.lineEditMDPConfirmation = QLineEdit(Dialog)
        self.lineEditMDPConfirmation.setObjectName(u"lineEditMDPConfirmation")
        self.lineEditMDPConfirmation.setGeometry(QRect(30, 320, 251, 31))
        self.lineEditCredits = QLineEdit(Dialog)
        self.lineEditCredits.setObjectName(u"lineEditCredits")
        self.lineEditCredits.setGeometry(QRect(30, 400, 251, 31))
        self.labelMDPConfirmation = QLabel(Dialog)
        self.labelMDPConfirmation.setObjectName(u"labelMDPConfirmation")
        self.labelMDPConfirmation.setGeometry(QRect(30, 290, 256, 31))
        self.labelMDPConfirmation.setFont(font1)
        self.labelCredit = QLabel(Dialog)
        self.labelCredit.setObjectName(u"labelCredit")
        self.labelCredit.setGeometry(QRect(30, 370, 256, 31))
        self.labelCredit.setFont(font1)
        self.buttonNewUser = QPushButton(Dialog)
        self.buttonNewUser.setObjectName(u"buttonNewUser")
        self.buttonNewUser.setGeometry(QRect(92, 440, 131, 31))
        self.buttonNewUser.setSizeIncrement(QSize(0, 0))
        self.buttonNewUser.setBaseSize(QSize(0, 0))
        self.buttonNewUser.raise_()
        self.labelTitle.raise_()
        self.labelPrenom.raise_()
        self.lineEditPrenom.raise_()
        self.labelIdentifiant.raise_()
        self.lineEditIdentifiant.raise_()
        self.labelMDP.raise_()
        self.lineEditMDP.raise_()
        self.lineEditMDPConfirmation.raise_()
        self.lineEditCredits.raise_()
        self.labelMDPConfirmation.raise_()
        self.labelCredit.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelTitle.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">=== Cr\u00e9ation d'un nouveau compte ===</p></body></html>", None))
        self.labelPrenom.setText(QCoreApplication.translate("Dialog", u"Prenom :", None))
        self.labelIdentifiant.setText(QCoreApplication.translate("Dialog", u"Identifiant :", None))
        self.labelMDP.setText(QCoreApplication.translate("Dialog", u"Mot de passe :", None))
        self.labelMDPConfirmation.setText(QCoreApplication.translate("Dialog", u"Confirmation :", None))
        self.labelCredit.setText(QCoreApplication.translate("Dialog", u"Credits :", None))
        self.buttonNewUser.setText(QCoreApplication.translate("Dialog", u"Cr\u00e9er le compte", None))
    # retranslateUi

