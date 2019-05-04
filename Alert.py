import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from menu import Ui_Menu
from sqlite3 import Error
from Alert_UI import Ui_Dialog
import sys
from AddRecords import AddRecords
import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Alert:
	def __init__(self):
		self.conn = sqlite3.connect('se_db.db')

		self.diag = QtWidgets.QDialog()
		self.table_ui = Ui_Dialog()
		self.table_ui.setupUi(self.diag)
		
		#self.viewRecords()
		#self.showdialog()
		self.diag.exec_()
		

	
	def addRecords(self):
		pop = AddRecords()
		self.viewRecords()
		
	def deleteRecords(self):
		r = self.table_ui.tableWidget.currentRow()
		id=self.table_ui.tableWidget.item(r,0).text()
		print(id)
		statement='DELETE FROM Prisoner WHERE ID=?'

		cur = self.conn.cursor()
		cur.execute(statement, (id,))
		self.conn.commit()
		self.viewRecords()

	def showdialog(self):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)

		msg.setText("This is a message box")
		msg.setInformativeText("This is additional information")
		msg.setWindowTitle("MessageBox demo")
		msg.setDetailedText("The details are as follows:")
		msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		msg.buttonClicked.connect(msgbtn)
		
		retval = msg.exec_()

	
	def viewRecords(self):
		print("hello")
		cur = self.conn.cursor()
		cur.execute("SELECT * from Staff")

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

			