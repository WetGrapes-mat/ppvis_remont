from view.view import View
from model.model import Model_U, Model_R


class ControllerRoom:
    def __init__(self, model):
        self.model = model
        self.view = View(self, self.model)

    def delet_room(self, room):
        pass

    def add_room(self, room):
        pass



class Controller:
    def __init__(self, model):
        self.model = model
        self.view = View(self, self.model)

    def start(self):
        self.view.show_start()

    def showPerconal(self):
        self.view.show_Perconal()

    def showCreateFlat(self):
        self.view.show_Create_flat()

    def showMainScreen(self, password, login):
        self.view.show_MainScreen()

    def showSelectType(self):
        self.view.show_SelectType()

    def showAddRoom(self):
        self.view.show_AddRoom()

    def showYourFlat(self):
        self.view.YourFlat()

    def showPrice(self, type_rep):
        self.view.PriceDialog()

    def showAutorizet(self):
        self.view.show_Autorizet()

    def showCreate(self):
        self.view.show_CreateAccountt()

    def showEnter(self):
        self.view.show_EnterAccount()




