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
		print(self.rights, "Rightsss value")

		name = self.ui.textEdit.toPlainText()

		job = self.ui.comboBox.currentText()
		access_level = self.ui.label.text() #Filhal Hardcoded
		cnic = self.ui.textEdit_4.toPlainText()
		
		if self.rights == 1: #edit mode
			mydata = self.data[0]
			date = mydata[8] #use old arrival date #CHECK THIS INDEX (8 tha tumne 4 rakha huwa tha)

		else: #new recird hai

			x = datetime.datetime.now()
			date = str(x.day)+"-"+str(x.month)+"-"+str(x.year)
		
		sal = (self.ui.textEdit_5.toPlainText())

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
		print("Date-----------",date)
		self.rr.append(date)
		self.rr.append(access_level)

		cur = self.conn.cursor()

		if(self.rights==0):

			cur.execute("Insert into Staff(staff_name,password,cnic,job,contact,salary,address,employment_date,access_level) VALUES (?,?,?,?,?,?,?,?,?)",self.rr)


			
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

			print(self.rr,"Old RR")


			print(newrr,"New RR")

			cur.execute("Update staff SET staff_name=?, password=?,cnic=?,job=?,contact=?,salary=?,address=?,employment_date=?,access_level=? WHERE staff_id=?",newrr)
		self.conn.commit()
		self.rr.clear()
		newrr.clear()

		

		
		


	def editRecord(self):
		
		print("hi")
		

		mydata = self.data[0]
		print("Data Received",self.data)
		ID = mydata[0]
		Name = mydata[1]
		password = mydata[2]
		CNIC = mydata[3]
		JOB = mydata[4]
		salary = mydata[5]
		contact = mydata[6]
		address = mydata[7]
		employment_date = mydata[8]

		print(employment_date,"Employement date")

		access_level = mydata[9]
		

		self.rr.append(ID)






		print(self.data)
		self.ui.textEdit.setText(str(Name))
		self.ui.textEdit_4.setText(str(CNIC))
		self.ui.textEdit_5.setText(str(contact))
		self.ui.textEdit_6.setText(str(salary))
		self.ui.textEdit_7.setText(str(address))

		index = self.ui.comboBox.findText(str(JOB))
		self.ui.comboBox.setCurrentIndex(index)

		


			