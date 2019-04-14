# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login_Ui(object):
    def setupUi(self, Login_Ui):
        Login_Ui.setObjectName("Login_Ui")
        Login_Ui.resize(350, 480)
        self.centralwidget = QtWidgets.QWidget(Login_Ui)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 150, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        Login_Ui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login_Ui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
        self.menubar.setObjectName("menubar")
        Login_Ui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login_Ui)
        self.statusbar.setObjectName("statusbar")
        Login_Ui.setStatusBar(self.statusbar)

        self.retranslateUi(Login_Ui)
        QtCore.QMetaObject.connectSlotsByName(Login_Ui)

    def retranslateUi(self, Login_Ui):
        _translate = QtCore.QCoreApplication.translate
        Login_Ui.setWindowTitle(_translate("Login_Ui", "MainWindow"))
        self.pushButton.setText(_translate("Login_Ui", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Ui = QtWidgets.QMainWindow()
    ui = Ui_Login_Ui()
    ui.setupUi(Login_Ui)
    Login_Ui.show()
    sys.exit(app.exec_())

