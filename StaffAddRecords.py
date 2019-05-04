import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from menu import Ui_Menu
from sqlite3 import Error
from table import Ui_Dialog
import sys
from StaffAddRecord_UI import Ui_Dialog
import datetime

import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class StaffAddRecords:
	def __init__(self,rights,data):
		self.conn = sqlite3.connect('se_db.db')
		self.rights = rights
		self.data = data
		
		self.rr = []
		self.diag = QtWidgets.QDialog()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self.diag)
		self.ui.pushButton.clicked.connect(self.AddRecord)
		self.ui.pushButton_4.clicked.connect(self.editRecord)
		
		self.ui.comboBox.addItems(["Admin", "Guard", "Other Staff"])
		self.ui.label.setText("0")
		self.ui.comboBox.currentIndexChanged.connect(self.updateLabel)

		if self.rights == 1:
			self.editRecord()

		self.diag.exec_()
	
	def updateLabel(self):
		self.ui.label.setText(str(self.ui.comboBox.currentIndex()))


				

	def AddRecord(self):
		

		## MODIFY THIS 

		name = self.ui.textEdit.toPlainText()

		job = self.ui.comboBox.currentText()
		access_level = self.ui.label.text() #Filhal Hardcoded
		cnic = self.ui.textEdit_4.toPlainText()
		
		if self.rights == 1: #edit mode
			mydata = self.data[0]
			date = mydata[4] #use old arrival date #CHECK THIS INDEX

		else: #new recird hai

			x = datetime.datetime.now()
			date = str(x.day)+"-"+str(x.month)+"-"+str(x.year)
		
		sal = int(self.ui.textEdit_5.toPlainText())

		contact = self.ui.textEdit_6.toPlainText()
		address = self.ui.textEdit_7.toPlainText()
		
		password = "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5" #12345

		newrr = []
		#rr.append(5)
		self.rr.append(name)
		self.rr.append(password)
		self.rr.append(cnic)
		self.rr.append(job)
		self.rr.append(sal)
		self.rr.append(contact)
		self.rr.append(address)
		self.rr.append(date)
		self.rr.append(access_level)

		cur = self.conn.cursor()

		if(self.rights==0):

			cur.execute("Insert into Staff(staff_name,password,cnic,job,salary,contact,address,employment_date,access_level) VALUES (?,?,?,?,?,?,?,?,?)",self.rr)


			
		else:
			#EditRecord
			
			
			iterator = 0
			
			#newrr.append(self.rr[0]) #ID at end

			for i in self.rr:
				if(iterator==0):
					None
				else:
					newrr.append(i)
				iterator = iterator + 1

			newrr.append(self.rr[0]) #ID at end

			cur.execute("Update Prisoner SET prisoner_name=?, section_id=?,cell_id=?,arrival_date=?,release_date=?,crime=?,crime_description=?,sentence=?,medical_status=?,emergency_name=?,work_assigned=?,Emergency_contact=?,Age=? WHERE prisoner_id=?",newrr)
		self.conn.commit()
		self.rr.clear()
		newrr.clear()

		self.ui.textEdit.clear()
		self.ui.textEdit_4.clear()
		self.ui.textEdit_5.clear()
		self.ui.textEdit_6.clear()
		self.ui.textEdit_7.clear()

		
		


	def editRecord(self):
		
		print("hi")
		

		mydata = self.data[0]
		print("Data Received",self.data)
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
		emg_Contact = mydata[12]
		work_Assigned = mydata[11]
		Age = mydata[13]

		self.rr.append(ID)






		print(self.data)
		self.ui.textEdit_4.setText(str(Age))
		self.ui.textEdit.setText(str(Name))
		self.ui.textEdit_5.setText(str(crime_desp))
		self.ui.textEdit_3.setText(str(sentence))
		self.ui.textEdit_6.setText(str(emg_Name))
		self.ui.textEdit_7.setText(str(emg_Contact))

		index = 0

		index = self.ui.comboBox.findText(str(section))
		self.ui.comboBox.setCurrentIndex(index)
		
		index = self.ui.comboBox_2.findText(str(cell))
		self.ui.comboBox_2.setCurrentIndex(index)

		index = self.ui.comboBox_3.findText(str(medical))
		self.ui.comboBox_3.setCurrentIndex(index)

		index = self.ui.comboBox_4.findText(str(crime))
		self.ui.comboBox_4.setCurrentIndex(index)

		index = self.ui.comboBox_5.findText(str(work_Assigned))
		self.ui.comboBox_5.setCurrentIndex(index)


		

		


			