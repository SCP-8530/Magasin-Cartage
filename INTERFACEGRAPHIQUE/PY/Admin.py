# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'INTERFACEGRAPHIQUE/UI/Admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(894, 620)
        self.textBrowserObjet = QtWidgets.QTextBrowser(Dialog)
        self.textBrowserObjet.setGeometry(QtCore.QRect(20, 50, 391, 541))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.textBrowserObjet.setFont(font)
        self.textBrowserObjet.setObjectName("textBrowserObjet")
        self.labelTitle = QtWidgets.QLabel(Dialog)
        self.labelTitle.setGeometry(QtCore.QRect(20, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.labelID = QtWidgets.QLabel(Dialog)
        self.labelID.setGeometry(QtCore.QRect(430, 80, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.labelID.setFont(font)
        self.labelID.setObjectName("labelID")
        self.labelType = QtWidgets.QLabel(Dialog)
        self.labelType.setGeometry(QtCore.QRect(430, 30, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.labelType.setFont(font)
        self.labelType.setObjectName("labelType")
        self.lineEditID = QtWidgets.QLineEdit(Dialog)
        self.lineEditID.setGeometry(QtCore.QRect(690, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditID.setFont(font)
        self.lineEditID.setObjectName("lineEditID")
        self.comboBoxType = QtWidgets.QComboBox(Dialog)
        self.comboBoxType.setGeometry(QtCore.QRect(690, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxType.setFont(font)
        self.comboBoxType.setObjectName("comboBoxType")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.labelErreur = QtWidgets.QLabel(Dialog)
        self.labelErreur.setGeometry(QtCore.QRect(430, 130, 441, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelErreur.setFont(font)
        self.labelErreur.setStyleSheet("color: rgb(255, 0, 0);\n"
"")
        self.labelErreur.setObjectName("labelErreur")
        self.buttonAjouter = QtWidgets.QPushButton(Dialog)
        self.buttonAjouter.setGeometry(QtCore.QRect(430, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonAjouter.setFont(font)
        self.buttonAjouter.setObjectName("buttonAjouter")
        self.buttonSupprimer = QtWidgets.QPushButton(Dialog)
        self.buttonSupprimer.setGeometry(QtCore.QRect(730, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonSupprimer.setFont(font)
        self.buttonSupprimer.setObjectName("buttonSupprimer")
        self.buttonModifier = QtWidgets.QPushButton(Dialog)
        self.buttonModifier.setGeometry(QtCore.QRect(580, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonModifier.setFont(font)
        self.buttonModifier.setObjectName("buttonModifier")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(430, 240, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.lineEdit1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit1.setGeometry(QtCore.QRect(650, 240, 221, 31))
        self.lineEdit1.setObjectName("lineEdit1")
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(430, 280, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.lineEdit2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit2.setGeometry(QtCore.QRect(650, 280, 221, 31))
        self.lineEdit2.setObjectName("lineEdit2")
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(430, 320, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.lineEdit3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit3.setGeometry(QtCore.QRect(650, 320, 221, 31))
        self.lineEdit3.setObjectName("lineEdit3")
        self.label4 = QtWidgets.QLabel(Dialog)
        self.label4.setGeometry(QtCore.QRect(430, 360, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.lineEdit5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit5.setGeometry(QtCore.QRect(650, 400, 221, 31))
        self.lineEdit5.setObjectName("lineEdit5")
        self.textEdit6 = QtWidgets.QTextEdit(Dialog)
        self.textEdit6.setGeometry(QtCore.QRect(650, 440, 221, 61))
        self.textEdit6.setObjectName("textEdit6")
        self.label5 = QtWidgets.QLabel(Dialog)
        self.label5.setGeometry(QtCore.QRect(430, 400, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(Dialog)
        self.label6.setGeometry(QtCore.QRect(430, 440, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.textEdit7 = QtWidgets.QTextEdit(Dialog)
        self.textEdit7.setGeometry(QtCore.QRect(650, 510, 221, 61))
        self.textEdit7.setObjectName("textEdit7")
        self.label7 = QtWidgets.QLabel(Dialog)
        self.label7.setGeometry(QtCore.QRect(430, 510, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.comboBox4 = QtWidgets.QComboBox(Dialog)
        self.comboBox4.setGeometry(QtCore.QRect(650, 360, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox4.setFont(font)
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelTitle.setText(_translate("Dialog", "Liste des Articles :"))
        self.labelID.setText(_translate("Dialog", "ID de l\'objet à affecter:"))
        self.labelType.setText(_translate("Dialog", "Type d\'object à afficher:"))
        self.comboBoxType.setItemText(0, _translate("Dialog", "Article"))
        self.comboBoxType.setItemText(1, _translate("Dialog", "Utilisateur"))
        self.comboBoxType.setItemText(2, _translate("Dialog", "Facture"))
        self.labelErreur.setText(_translate("Dialog", "* labelErreur"))
        self.buttonAjouter.setText(_translate("Dialog", "Ajouter"))
        self.buttonSupprimer.setText(_translate("Dialog", "Supprimer"))
        self.buttonModifier.setText(_translate("Dialog", "Modifier"))
        self.label1.setText(_translate("Dialog", "Label 1"))
        self.label2.setText(_translate("Dialog", "Label 2"))
        self.label3.setText(_translate("Dialog", "Label 3"))
        self.label4.setText(_translate("Dialog", "Type:"))
        self.label5.setText(_translate("Dialog", "Label 5"))
        self.label6.setText(_translate("Dialog", "Label 6"))
        self.label7.setText(_translate("Dialog", "Label 7"))
        self.comboBox4.setItemText(0, _translate("Dialog", "Pierre Magique"))
        self.comboBox4.setItemText(1, _translate("Dialog", "Potion"))
        self.comboBox4.setItemText(2, _translate("Dialog", "Sortillege"))
