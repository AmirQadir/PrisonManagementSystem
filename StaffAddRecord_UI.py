# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StaffAddRecord_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 353)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 401, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(13)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.textEdit_4 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_4.setObjectName("textEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_4)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.textEdit_5 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_5.setObjectName("textEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit_5)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.textEdit_6 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_6.setObjectName("textEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textEdit_6)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.textEdit_7 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_7.setObjectName("textEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.textEdit_7)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_4.setText(_translate("Dialog", "Job"))
        self.label_5.setText(_translate("Dialog", "Access Level"))
        self.label_6.setText(_translate("Dialog", "CNIC"))
        self.label_9.setText(_translate("Dialog", "Salary"))
        self.label_11.setText(_translate("Dialog", "Contact"))
        self.label_10.setText(_translate("Dialog", "Address"))
        self.pushButton.setText(_translate("Dialog", "Insert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

