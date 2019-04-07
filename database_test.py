import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from sqlite3 import Error
from table import Ui_Dialog
from AddRecord_UI import Ui_Dialog
import sys

import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


def create_connection(file_name):
	try:
		conn = sqlite3.connect(file_name)
		return conn
	except Error as e:
		print(e)

	None
#conn = sqlite3.connect('prison.db')
file_path = 'C:\\Users\\Razor\\Desktop\\Prison.db'
conn = create_connection(file_path)


def addRecord():
	print("WElcome")

def viewRecord():
	print("hello")
	cur = conn.cursor()
	cur.execute("SELECT * from Prisoner")

	rows = cur.fetchall()

	ui.tableWidget.setRowCount(len(rows)) #Number of records jitna

	itr1 = 0
	itr2 = 0
	for record in rows:
		itr2 = 0
		for eachrecord in record:
			print(eachrecord," ..")
			ui.tableWidget.setItem(itr1,itr2,QTableWidgetItem(str(eachrecord)))
			itr2 = itr2 + 1
			print("I am here", str(eachrecord))
		itr1 = itr1 + 1

		print(record,'---')
	#ui.tableWidget.addRow("")
	#ui.tableWidget.setItem(0,0,QTableWidgetItem("TEXT"))

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
ui.pushButton.clicked.connect(viewRecord)
ui.pushButton_2.clicked.connect(addRecord)
Dialog.show()
sys.exit(app.exec_())



# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()



