# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 539)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowserInventaire = QTextBrowser(self.centralwidget)
        self.textBrowserInventaire.setObjectName(u"textBrowserInventaire")
        self.textBrowserInventaire.setGeometry(QRect(20, 60, 401, 441))
        self.labelTitre = QLabel(self.centralwidget)
        self.labelTitre.setObjectName(u"labelTitre")
        self.labelTitre.setGeometry(QRect(20, 20, 401, 31))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(15)
        self.labelTitre.setFont(font)
        self.buttonAjouter = QPushButton(self.centralwidget)
        self.buttonAjouter.setObjectName(u"buttonAjouter")
        self.buttonAjouter.setGeometry(QRect(450, 190, 151, 31))
        self.lineEditID = QLineEdit(self.centralwidget)
        self.lineEditID.setObjectName(u"lineEditID")
        self.lineEditID.setGeometry(QRect(570, 60, 161, 31))
        self.lineEditQuantite = QLineEdit(self.centralwidget)
        self.lineEditQuantite.setObjectName(u"lineEditQuantite")
        self.lineEditQuantite.setGeometry(QRect(570, 100, 161, 31))
        self.labelID = QLabel(self.centralwidget)
        self.labelID.setObjectName(u"labelID")
        self.labelID.setGeometry(QRect(450, 60, 121, 31))
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(10)
        self.labelID.setFont(font1)
        self.labelQuantite = QLabel(self.centralwidget)
        self.labelQuantite.setObjectName(u"labelQuantite")
        self.labelQuantite.setGeometry(QRect(450, 100, 121, 31))
        self.labelQuantite.setFont(font1)
        self.textBrowserPanier = QTextBrowser(self.centralwidget)
        self.textBrowserPanier.setObjectName(u"textBrowserPanier")
        self.textBrowserPanier.setGeometry(QRect(450, 310, 321, 192))
        self.labelPanier = QLabel(self.centralwidget)
        self.labelPanier.setObjectName(u"labelPanier")
        self.labelPanier.setGeometry(QRect(450, 270, 321, 31))
        self.labelPanier.setFont(font)
        self.labelErreur = QLabel(self.centralwidget)
        self.labelErreur.setObjectName(u"labelErreur")
        self.labelErreur.setGeometry(QRect(430, 140, 321, 31))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setBold(True)
        font2.setWeight(75)
        self.labelErreur.setFont(font2)
        self.labelErreur.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.buttonRetirer = QPushButton(self.centralwidget)
        self.buttonRetirer.setObjectName(u"buttonRetirer")
        self.buttonRetirer.setGeometry(QRect(620, 190, 151, 31))
        self.buttonPayer = QPushButton(self.centralwidget)
        self.buttonPayer.setObjectName(u"buttonPayer")
        self.buttonPayer.setGeometry(QRect(450, 230, 151, 31))
        self.buttonFacture = QPushButton(self.centralwidget)
        self.buttonFacture.setObjectName(u"buttonFacture")
        self.buttonFacture.setGeometry(QRect(620, 230, 151, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTitre.setText(QCoreApplication.translate("MainWindow", u"Liste des produits en vente", None))
        self.buttonAjouter.setText(QCoreApplication.translate("MainWindow", u"Ajout\u00e9 au panier", None))
        self.labelID.setText(QCoreApplication.translate("MainWindow", u"ID du produit:", None))
        self.labelQuantite.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9:", None))
        self.labelPanier.setText(QCoreApplication.translate("MainWindow", u"Panier", None))
        self.labelErreur.setText(QCoreApplication.translate("MainWindow", u"* labelErreur", None))
        self.buttonRetirer.setText(QCoreApplication.translate("MainWindow", u"Retirer du panier", None))
        self.buttonPayer.setText(QCoreApplication.translate("MainWindow", u"Payer", None))
        self.buttonFacture.setText(QCoreApplication.translate("MainWindow", u"Voir mes factures", None))
    # retranslateUi

