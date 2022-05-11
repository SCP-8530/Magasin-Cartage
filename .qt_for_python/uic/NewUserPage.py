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
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 311, 31))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 256, 31))
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 80, 251, 31))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 130, 256, 31))
        self.label_3.setFont(font1)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 160, 251, 31))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 210, 256, 31))
        self.label_4.setFont(font1)
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 240, 251, 31))
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 320, 251, 31))
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 400, 251, 31))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 290, 256, 31))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 370, 256, 31))
        self.label_6.setFont(font1)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(92, 440, 131, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">=== Cr\u00e9ation d'un nouveau compte ===</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Prenom:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Identifiant:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Mot de passe:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Confirmation:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Credit:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
    # retranslateUi

