# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys

import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_Dialog(object):
    def LoginSuccess(self):
        print(self.lineEdit.text())
        print(self.textEdit.toPlainText())
        if(self.textEdit.toPlainText()=="Amir" and self.lineEdit.text()=="12345"):
            print("HI")
            #self.lineEdit.setText("aaSuccess")
            print("Something")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(833, 737)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(110, 180, 571, 81))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 450, 187, 57))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 320, 561, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.LoginSuccess)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


