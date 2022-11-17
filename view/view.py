from view.screen.add_room import Ui_add_room
from view.screen.autorizet import Ui_autorizet
from view.screen.create_acount import Ui_create_acount
from view.screen.create_flat import Ui_create_flat
from view.screen.enter_account import Ui_enter_account
from view.screen.main_scrin import Ui_main_scrin
from view.screen.perconal import Ui_perconal
from view.screen.select_type import Ui_select_type
from view.screen.your_flat import Ui_your_flat
from view.screen.price_diatlod import Ui_Dialog


import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class View:
    def __init__(self, c, m):
        self.model = m
        self.controller = c

        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()

        self.MainScreen = Ui_main_scrin(self.controller,self.model)
        self.AddRoomScreen = Ui_add_room(self.controller,self.model)
        self.Autorizet = Ui_autorizet(self.controller,self.model)
        self.CreateAcount = Ui_create_acount(self.controller,self.model)
        self.CreateFlat = Ui_create_flat(self.controller,self.model)
        self.Perconal = Ui_perconal(self.controller,self.model)
        self.SelectType = Ui_select_type(self.controller,self.model)
        self.YourFlat = Ui_your_flat(self.controller,self.model)
        self.EnterAccount = Ui_enter_account(self.controller,self.model)
        self.PriceDialog = Ui_Dialog(self.controller,self.model)









    def show_start(self):
        self.Autorizet.show()
        sys.exit(self.app.exec_())

    def show_Perconal(self):
        self.MainScreen.hide()
        self.Perconal.show()

    def show_Create_flat(self):
        self.MainScreen.hide()
        self.YourFlat.hide()
        self.SelectType.hide()
        self.AddRoomScreen.hide()
        self.CreateFlat.show()

    def show_MainScreen(self):
        self.CreateAcount.hide()
        self.EnterAccount.hide()
        self.Autorizet.hide()
        self.CreateFlat.hide()
        self.Perconal.hide()
        self.MainScreen.show()

    def show_AddRoom(self):
        self.CreateFlat.hide()
        self.AddRoomScreen.show()

    def show_YourFlat(self):
        self.CreateFlat.hide()
        self.YourFlat.show()

    def show_SelectType(self):
        self.CreateFlat.hide()
        self.SelectType.show()

    def show_Price(self):
        self.PriceDialog.show()

    def show_EnterAccount(self):
        self.Autorizet.hide()
        self.EnterAccount.show()

    def show_CreateAccountt(self):
        self.Autorizet.hide()
        self.CreateAcount.show()

    def show_Autorizet(self):
        self.CreateAcount.hide()
        self.EnterAccount.hide()
        self.Autorizet.show()
