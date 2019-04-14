# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddRecord_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from sqlite3 import Error



import sys

import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# def create_connection(file_name):
#     try:
#         conn = sqlite3.connect(file_name)
#         return conn
#     except Error as e:
#         print(e)

    # None
class Ui_Dialog2(object):
    def AddRecord(self):
        conn = sqlite3.connect('prison.db')
        name = self.textEdit_2.toPlainText()
        sentence = int(self.textEdit_3.toPlainText())
        rr = []

        rr.append(name)
        rr.append(sentence)

        cur = conn.cursor()
        cur.execute("Insert into Prisoner(Name,Sentence) VALUES (?,?)",rr)
        conn.commit()

        print("Vip")



    def setupUi2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 130, 111, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(223, 190, 121, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 190, 47, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.AddRecord)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "Sentence"))
        self.label_4.setText(_translate("Dialog", "Years"))
        self.pushButton.setText(_translate("Dialog", "Insert"))

#file_path = 'C:\\Users\\Razor\\Desktop\\Prison.db'
#conn = create_connection(file_path)


if __name__ == "__main__":
    import sys
    
    #conn = sqlite3.connect('prison.db')

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi2(Dialog)
    ui.pushButton.clicked.connect(ui.AddRecord)
    Dialog.show()
    sys.exit(app.exec_())


