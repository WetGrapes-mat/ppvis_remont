# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_flat.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel, QWidget)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_create_flat(QMainWindow, object):
    def __init__(self, c, m):
        super().__init__()
        self.model = m
        self.controller = c
        create_flat = QWidget()


        self.setObjectName("RemontIP")
        self.resize(330, 480)
        self.centralwidget = QtWidgets.QWidget(create_flat)
        self.centralwidget.setStyleSheet("background-color: rgb(154, 151, 153);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(30, 70, 271, 161))
        self.image.setMinimumSize(QtCore.QSize(201, 0))
        self.image.setStyleSheet("")
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("view/screen/img/thumbnail-1.jpg.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.add_room_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_room_btn.setGeometry(QtCore.QRect(80, 250, 171, 51))
        self.add_room_btn.setStyleSheet("background-color: rgba(62, 132, 91, 217);\n"
"color: rgb(255, 255, 255);")
        self.add_room_btn.setObjectName("add_room_btn")
        self.add_room_btn.clicked.connect(lambda: self.controller.showAddRoom())

        self.show_flat_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_flat_btn.setGeometry(QtCore.QRect(80, 320, 171, 51))
        self.show_flat_btn.setStyleSheet("background-color: rgba(61, 131, 90, 217);\n"
"color: rgb(255, 255, 255);")
        self.show_flat_btn.setObjectName("show_flat_btn")
        self.show_flat_btn.clicked.connect(lambda: self.controller.showYourFlat())
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(180, 10, 131, 40))
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
        self.back_btn.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.back_btn.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(lambda: self.controller.showMainScreen(1,2))

        self.calculate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_btn.setGeometry(QtCore.QRect(80, 390, 171, 51))
        self.calculate_btn.setStyleSheet("background-color: rgba(62, 132, 91, 217);\n"
"color: rgb(255, 255, 255);")
        self.calculate_btn.setObjectName("calculate_btn")
        self.calculate_btn.clicked.connect(lambda: self.controller.showSelectType())

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(create_flat)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.add_room_btn.setText(_translate("RemontIP", "Add Room"))
        self.show_flat_btn.setText(_translate("RemontIP", "Show Flat"))
        self.text.setText(_translate("RemontIP", "<html><head/><body><p><span style=\" font-size:24pt;\">Create Flat</span></p></body></html>"))
        self.back_btn.setText(_translate("RemontIP", "<"))
        self.calculate_btn.setText(_translate("RemontIP", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemontIP = QtWidgets.QMainWindow()
    ui = Ui_create_flat()
    ui.setupUi(RemontIP)
    RemontIP.show()
    sys.exit(app.exec_())
