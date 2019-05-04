import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from menu import Ui_Menu
from sqlite3 import Error
from StaffRecords_UI import Ui_Dialog
import sys
from AddRecords import AddRecords
import PyQt5
from StaffAddRecords import StaffAddRecords

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class StaffRecords:
	def __init__(self):
		self.conn = sqlite3.connect('se_db.db')

		self.diag = QtWidgets.QDialog()
		self.table_ui = Ui_Dialog()
		self.table_ui.setupUi(self.diag)
		self.table_ui.pushButton.clicked.connect(self.viewRecords)
		self.table_ui.pushButton_2.clicked.connect(self.addRecords)
		self.table_ui.pushButton_3.clicked.connect(self.deleteRecords)
		self.table_ui.pushButton_4.clicked.connect(self.editRecords)

		self.viewRecords()
		self.diag.exec_()
		

	
	def addRecords(self):
		pop = StaffAddRecords(0,None)
		self.viewRecords()
		
	def deleteRecords(self):
		r = self.table_ui.tableWidget.currentRow()
		id=self.table_ui.tableWidget.item(r,0).text()
		print(id)
		statement='DELETE FROM Staff WHERE staff_id=?'

		cur = self.conn.cursor()
		cur.execute(statement, (id,))
		self.conn.commit()
		self.viewRecords()

	
	def viewRecords(self):
		print("hello")
		cur = self.conn.cursor()
		cur.execute("SELECT staff_id , staff_name, job, contact, address, cnic, salary, employment_date from Staff")

		rows = cur.fetchall()

		self.table_ui.tableWidget.setRowCount(len(rows)) #Number of records jitna

		itr1 = 0
		itr2 = 0
		for record in rows:
			itr2 = 0
			for eachrecord in record:
				print(eachrecord," ..")
				self.table_ui.tableWidget.setItem(itr1,itr2,QTableWidgetItem(str(eachrecord)))
				itr2 = itr2 + 1
				# print("I am here", str(eachrecord))
			itr1 = itr1 + 1

	def editRecords(self):
		print("Me editRecords")
		try:
			print("Arrived in try")
			selectedRow = self.table_ui.tableWidget.currentRow()
			unique_id = self.table_ui.tableWidget.item(selectedRow,0).text()
			statement='SELECT * FROM staff WHERE staff_id=?'
			cur = self.conn.cursor()

			cur.execute(statement, (unique_id,))
			data = cur.fetchall() #selected row


			pops = StaffAddRecords(1,data)
			print("HI")
		except:
			print("can't be edited")

		self.viewRecords()


			