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
        Login_Ui.resize(387, 517)
        self.centralwidget = QtWidgets.QWidget(Login_Ui)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 110, 301, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 410, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        Login_Ui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login_Ui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 21))
        self.menubar.setObjectName("menubar")
        Login_Ui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login_Ui)
        self.statusbar.setObjectName("statusbar")
        Login_Ui.setStatusBar(self.statusbar)

        self.retranslateUi(Login_Ui)
        self.lineEdit_2.returnPressed.connect(self.pushButton.click)
        QtCore.QMetaObject.connectSlotsByName(Login_Ui)

    def retranslateUi(self, Login_Ui):
        _translate = QtCore.QCoreApplication.translate
        Login_Ui.setWindowTitle(_translate("Login_Ui", "MainWindow"))
        self.label.setText(_translate("Login_Ui", "Username:"))
        self.label_2.setText(_translate("Login_Ui", "Password:"))
        self.pushButton.setText(_translate("Login_Ui", "Login"))
        self.label_3.setText(_translate("Login_Ui", "Prison Management System"))
        self.label_4.setText(_translate("Login_Ui", "For login issues contact the admin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Ui = QtWidgets.QMainWindow()
    ui = Ui_Login_Ui()
    ui.setupUi(Login_Ui)
    Login_Ui.show()
    sys.exit(app.exec_())

