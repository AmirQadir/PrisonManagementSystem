import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from menu import Ui_Menu
from sqlite3 import Error
from table import Ui_Dialog
import sys
from AddRecords import AddRecords
import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class PrisonerRecords:
	def __init__(self,access_level):
		#self.conn = sqlite3.connect('prison.db')
		self.conn = sqlite3.connect('se_db.db')
		
		print("I am here",access_level)

		self.diag = QtWidgets.QDialog()
		self.table_ui = Ui_Dialog()
		self.table_ui.setupUi(self.diag)
		self.table_ui.pushButton.clicked.connect(self.viewRecords)
		if(access_level!=0):
			self.table_ui.pushButton_2.setEnabled(False)
			self.table_ui.pushButton_4.setEnabled(False)
			self.table_ui.pushButton_3.setEnabled(False)
		else:
			self.table_ui.pushButton_2.clicked.connect(self.addRecords)
			self.table_ui.pushButton_4.clicked.connect(self.editRecords)
			self.table_ui.pushButton_3.clicked.connect(self.deleteRecords)
		self.table_ui.pushButton_5.clicked.connect(self.searchRecords)


		self.viewRecords()
		self.diag.exec_()
		

	def addRecords(self):
		data = None

		pop = AddRecords(0,data)
		self.viewRecords()
		
	def deleteRecords(self):
		r = self.table_ui.tableWidget.currentRow()
		id=self.table_ui.tableWidget.item(r,0).text()
		print(id)
		statement='DELETE FROM prisoner WHERE prisoner_id=?'

		cur = self.conn.cursor()
		cur.execute(statement, (id,))
		self.conn.commit()
		self.viewRecords()

	def searchRecords(self):
		data = self.table_ui.textEdit.toPlainText()
		cur = self.conn.cursor()
		statement = 'SELECT * from prisoner WHERE ID=? OR NAME=?'
		cur.execute(statement, (data,data))

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


		selectedRow = self.table_ui.tableWidget.currentRow()
		unique_id = self.table_ui.tableWidget.item(selectedRow,0).text()
		statement='SELECT * FROM prisoner WHERE prisoner_id=?'
		cur = self.conn.cursor()

		cur.execute(statement, (unique_id,))
		data = cur.fetchall() #selected row


		pops = AddRecords(1,data)
		print("HI")
		self.viewRecords()



	def viewRecords(self):
	
		cur = self.conn.cursor()
		cur.execute("SELECT * from Prisoner")

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

			