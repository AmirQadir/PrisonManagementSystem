# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys

import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_mainDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.video_surv = QtWidgets.QPushButton(Dialog)
        self.video_surv.setGeometry(QtCore.QRect(130, 30, 141, 51))
        self.video_surv.setObjectName("video_surv")
        self.prisoner_info = QtWidgets.QPushButton(Dialog)
        self.prisoner_info.setGeometry(QtCore.QRect(130, 110, 141, 51))
        self.prisoner_info.setObjectName("prisoner_info")
        self.guards_info = QtWidgets.QPushButton(Dialog)
        self.guards_info.setGeometry(QtCore.QRect(130, 190, 141, 51))
        self.guards_info.setObjectName("guards_info")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main Menu"))
        self.video_surv.setText(_translate("Dialog", "Video Surveillance"))
        self.prisoner_info.setText(_translate("Dialog", "Prisoners\' Information"))
        self.guards_info.setText(_translate("Dialog", "Guards\' Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_mainDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

