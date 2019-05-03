import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from menu import Ui_Menu
from sqlite3 import Error
from table import Ui_Dialog
import sys
from AddRecord_UI import Ui_Dialog
import datetime

import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class AddRecords:
	def __init__(self,rights,data):
		self.conn = sqlite3.connect('se_db.db')
		self.rights = rights
		self.data = data
		
		self.rr = []
		self.diag = QtWidgets.QDialog()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self.diag)
		self.ui.pushButton.clicked.connect(self.AddRecord)
		if self.rights == 1:
			self.editRecord()

		self.diag.exec_()
	
	def AddRecord(self):
		name = self.ui.textEdit.toPlainText()
		section_ID = 1
		cell_ID = 1 #Filhal Hardcoded
		#arrival_Date = '09/11'
		x = datetime.datetime.now()
		arrival_Date = str(x.day)+"-"+str(x.month)+"-"+str(x.year)
		Crime = 'Shararti'
		crime_description = self.ui.textEdit_5.toPlainText()
		sentence = int(self.ui.textEdit_3.toPlainText())
		Medical_Status = 'Bemaar'
		Emergency_contact_name = self.ui.textEdit_6.toPlainText()
		duty_assigned = 'IDK'

		age = (self.ui.textEdit_4.toPlainText())
		Emergency_contact_number = self.ui.textEdit_7.toPlainText()
		release_Date = str(x.day)+"-"+str(x.month)+"-"+str(x.year+sentence)
		

		newrr = []
		#rr.append(5)
		self.rr.append(name)
		self.rr.append(section_ID)
		self.rr.append(cell_ID)
		self.rr.append(arrival_Date)
		self.rr.append(release_Date)
		self.rr.append(Crime)
		self.rr.append(crime_description)
		self.rr.append(sentence)
		self.rr.append(Medical_Status)
		self.rr.append(Emergency_contact_name)
		self.rr.append(duty_assigned)

		self.rr.append(age)

		self.rr.append(Emergency_contact_number)

		cur = self.conn.cursor()

		if(self.rights==0):

			cur.execute("Insert into Prisoner(prisoner_name,section_id,cell_id,arrival_date,release_date,crime,crime_description,sentence,medical_status,emergency_name,work_assigned,Emergency_contact,Age) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",self.rr)


			
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
		self.ui.textEdit_3.clear()
		self.ui.textEdit_4.clear()
		self.ui.textEdit_5.clear()
		self.ui.textEdit_6.clear()
		self.ui.textEdit_7.clear()

		
		


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
		emg_Contact = mydata[11]
		work_Assigned = mydata[12]
		Age = mydata[13]

		self.rr.append(ID)






		print(self.data)
		self.ui.textEdit_4.setText(str(Age))
		self.ui.textEdit.setText(str(Name))
		self.ui.textEdit_5.setText(str(crime_desp))
		self.ui.textEdit_3.setText(str(sentence))
		self.ui.textEdit_6.setText(str(emg_Name))
		self.ui.textEdit_7.setText(str(emg_Contact))





		

		


			