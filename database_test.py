import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from table import Ui_Dialog
import sys

conn = sqlite3.connect('prison.db')

c = conn.cursor()

def testfunc():
	print("hello")
	c.execute("SELECT * from Prisoner")
	#ui.tableWidget.addRow("")
	ui.tableWidget.setRowCount(4)
	ui.tableWidget.setItem(0,1,QTableWidgetItem("TEXT"))

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
ui.pushButton.clicked.connect(testfunc)
Dialog.show()
sys.exit(app.exec_())



# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()



