import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from menu import Ui_Menu
from sqlite3 import Error
from table import Ui_Dialog
import sys
from AddRecord_UI import Ui_Dialog

import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class AddRecords:
	def __init__(self):
		self.conn = sqlite3.connect('prison.db')

		self.diag = QtWidgets.QDialog()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self.diag)
		self.ui.pushButton.clicked.connect(self.AddRecord)
		self.diag.exec_()

	def AddRecord(self):
		name = self.ui.textEdit_2.toPlainText()
		sentence = int(self.ui.textEdit_3.toPlainText())
		rr = []

		rr.append(name)
		rr.append(sentence)

		cur = self.conn.cursor()
		cur.execute("Insert into Prisoner(Name,Sentence) VALUES (?,?)",rr)
		self.conn.commit()


		self.ui.textEdit_2.clear()
		self.ui.textEdit_3.clear()
		


			