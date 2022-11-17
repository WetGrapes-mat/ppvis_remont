# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter_account.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_enter_account(QMainWindow, object):
    def __init__(self, c, m):
        super().__init__()
        self.model = m
        self.controller = c
        enter_account = QWidget()

        self.setObjectName("RemontIP")
        self.resize(330, 480)
        self.centralwidget = QtWidgets.QWidget(enter_account)
        self.centralwidget.setStyleSheet("background-color: rgb(154, 151, 153);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(90, 180, 151, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        self.text.setBaseSize(QtCore.QSize(0, 0))
        self.text.setTabletTracking(False)
        self.text.setAcceptDrops(False)
        self.text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text.setStyleSheet("color: rgb(255, 255, 255);")
        self.text.setLineWidth(1)
        self.text.setTextFormat(QtCore.Qt.AutoText)
        self.text.setScaledContents(False)
        self.text.setObjectName("text")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(60, 340, 91, 51))
        self.back_btn.setStyleSheet("background-color: rgba(62, 132, 91, 217);\n"
"color: rgb(255, 255, 255);")
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(lambda: self.controller.showAutorizet())

        self.Room_type = QtWidgets.QLineEdit(self.centralwidget)
        self.Room_type.setGeometry(QtCore.QRect(70, 230, 191, 31))
        self.Room_type.setStyleSheet("border: 3px solid;\n"
"border-color: rgba(64, 138, 95, 217);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Stencil\";\n"
"color: gray;\n"
"")
        self.Room_type.setFrame(True)
        self.Room_type.setObjectName("Room_type")
        self.lineEdit_height = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_height.setGeometry(QtCore.QRect(70, 270, 191, 31))
        self.lineEdit_height.setStyleSheet("border: 3px solid;\n"
"border-color: rgba(64, 138, 95, 217);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Stencil\";\n"
"color: gray;\n"
"")
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.log_in_btn = QtWidgets.QPushButton(self.centralwidget)
        self.log_in_btn.setGeometry(QtCore.QRect(180, 340, 91, 51))
        self.log_in_btn.setStyleSheet("background-color: rgba(62, 132, 91, 217);\n"
"color: rgb(255, 255, 255);")
        self.log_in_btn.setObjectName("log_in_btn")
        self.log_in_btn.clicked.connect(lambda: self.controller.showMainScreen(1,2))
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(enter_account)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.text.setText(_translate("RemontIP", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Enter account</span></p></body></html>"))
        self.back_btn.setText(_translate("RemontIP", "Back"))
        self.Room_type.setText(_translate("RemontIP", "Enter e-mail or ph. number..."))
        self.lineEdit_height.setText(_translate("RemontIP", "Enter password..."))
        self.log_in_btn.setText(_translate("RemontIP", "Log in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemontIP = QtWidgets.QMainWindow()
    ui = Ui_enter_account()
    ui.setupUi(RemontIP)
    RemontIP.show()
    sys.exit(app.exec_())
