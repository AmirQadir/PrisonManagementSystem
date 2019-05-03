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
	def __init__(self,rights,data):
		self.conn = sqlite3.connect('prison.db')
		self.rights = rights
		self.data = data
		

		self.diag = QtWidgets.QDialog()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self.diag)
		self.ui.pushButton.clicked.connect(self.AddRecord)
		if self.rights == 1:
			self.editRecord()

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


	def editRecord(self):
		
		print("hi")
		'''
			name -> textEdit
			age -> textEdit_4
			crime description -> textEdit5
			sentence -> textEdit3
			Emergency contact Name-> textEdit6
			Emergency contact Number-> textEdit7


		for record in data:
			itr = 0
			for eachrecord in data:
				if(itr==0 or itr==2 or itr==3 or itr==5 or itr==6 or itr==1):
					print("I am here")
				else:
					self.ui.textEdit_4.setText("Amir")


	
			'''

		mydata = self.data[0]
		ID = mydata[0]
		Name = mydata[1]
		section = mydata[2]
		cell = mydata[3]
		A_date = mydata[4]
		R_date = mydata[5]
		crime = mydata[6]
		crime_desp = mydata[7]
		sentence = mydata[8]

		medical = mydata[9]
		emg_Name = mydata[10]
		emg_Contact = mydata[11]
		work_Assigned = mydata[12]
		Age = mydata[13]







		print(self.data)
		self.ui.textEdit_4.setText(str(Age))
		self.ui.textEdit.setText(str(Name))
		self.ui.textEdit_5.setText(str(crime_desp))
		self.ui.textEdit_3.setText(str(sentence))
		self.ui.textEdit_6.setText(str(emg_Name))
		self.ui.textEdit_7.setText(str(emg_Contact))



		

		


			