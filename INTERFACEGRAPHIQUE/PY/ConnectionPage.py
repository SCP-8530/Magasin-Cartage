# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'INTERFACEGRAPHIQUE/UI/ConnectionPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(359, 265)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 210, 341, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.BoiteABouton = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.BoiteABouton.setContentsMargins(0, 0, 0, 0)
        self.BoiteABouton.setObjectName("BoiteABouton")
        self.buttonConnection = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonConnection.setObjectName("buttonConnection")
        self.BoiteABouton.addWidget(self.buttonConnection)
        self.buttonNouveauCompte = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonNouveauCompte.setObjectName("buttonNouveauCompte")
        self.BoiteABouton.addWidget(self.buttonNouveauCompte)
        self.labelIdentifiant = QtWidgets.QLabel(Dialog)
        self.labelIdentifiant.setGeometry(QtCore.QRect(70, 20, 199, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.labelIdentifiant.setFont(font)
        self.labelIdentifiant.setObjectName("labelIdentifiant")
        self.labelMotDePasse = QtWidgets.QLabel(Dialog)
        self.labelMotDePasse.setGeometry(QtCore.QRect(70, 100, 199, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.labelMotDePasse.setFont(font)
        self.labelMotDePasse.setObjectName("labelMotDePasse")
        self.lineEditIdentifiant = QtWidgets.QLineEdit(Dialog)
        self.lineEditIdentifiant.setGeometry(QtCore.QRect(70, 60, 201, 31))
        self.lineEditIdentifiant.setObjectName("lineEditIdentifiant")
        self.lineEditMotDePasse = QtWidgets.QLineEdit(Dialog)
        self.lineEditMotDePasse.setGeometry(QtCore.QRect(70, 140, 201, 31))
        self.lineEditMotDePasse.setObjectName("lineEditMotDePasse")
        self.labelErreur = QtWidgets.QLabel(Dialog)
        self.labelErreur.setGeometry(QtCore.QRect(70, 180, 231, 21))
        self.labelErreur.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelErreur.setObjectName("labelErreur")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.buttonConnection.setText(_translate("Dialog", "Se connecter"))
        self.buttonNouveauCompte.setText(_translate("Dialog", "Créer un nouveau compte"))
        self.labelIdentifiant.setText(_translate("Dialog", "Identifiant :"))
        self.labelMotDePasse.setText(_translate("Dialog", "Mot de passe :"))
        self.labelErreur.setText(_translate("Dialog", "* Identifiant ou mot de passe incorrecte"))
