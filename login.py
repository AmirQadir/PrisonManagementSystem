# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mainmenu import Ui_mainDialog


import sys

import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Ui_Dialog(object):
    def gotoMainMenu(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_mainDialog()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(623, 356)
        self.userNameLabel = QtWidgets.QLabel(Dialog)
        self.userNameLabel.setGeometry(QtCore.QRect(150, 120, 61, 31))
        self.userNameLabel.setObjectName("userNameLabel")
        self.userPasswordLabel = QtWidgets.QLabel(Dialog)
        self.userPasswordLabel.setGeometry(QtCore.QRect(150, 170, 61, 16))
        self.userPasswordLabel.setObjectName("userPasswordLabel")
        self.userName = QtWidgets.QLineEdit(Dialog)
        self.userName.setGeometry(QtCore.QRect(280, 120, 113, 20))
        self.userName.setObjectName("userName")
        self.userPassword = QtWidgets.QLineEdit(Dialog)
        self.userPassword.setGeometry(QtCore.QRect(280, 170, 113, 20))
        self.userPassword.setObjectName("userPassword")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(300, 230, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.gotoMainMenu)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Prisoner Managment System"))
        self.userNameLabel.setText(_translate("Dialog", "User Name"))
        self.userPasswordLabel.setText(_translate("Dialog", "Password"))
        self.loginButton.setWhatsThis(_translate("Dialog", "Login Button"))
        self.loginButton.setText(_translate("Dialog", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

