from enum import Enum

class Consumer:
    def __init__(self, id, type, password, login, phone, userName , Name):
        self.id = id
        self.userType = type
        self.password = password
        self.login = login
        self.mobPhone = phone
        self.userName = userName
        self.Name = Name


class User(Consumer):
    def __init__(self, id, type, password, login, phone, userName , Name):
        super().__init__(self, id, type, password, login, phone, userName , Name)
        self.rooms = RoomStorage()



class Admin(Consumer):
    def __init__(self, id, type, password, login, phone, userName , Name):
        super().__init__(self, id, type, password, login, phone, userName , Name)


class UsersStorage:
    def __init__(self):
        self.UserStorage = []
        self.AdminStorage = []


class RoomStorage:
    def __init__(self):
        self.RoomsStorage = []


class Room:
    def __init__(self, type, length, width, height):
        self.type = RoomType(type)
        self.length = length
        self.width = width
        self.height = height


class RoomType(Enum):
    bathroom = 1
    kitchen = 2
    living_room = 3
    corridor = 4
    wardrobe = 5


class Model_U:
    def __init__(self):
        self.users_storage = UsersStorage()

    def add_user(self, user):
        pass

    def calc(self, user, type_repair):
        pass


class Model_R:
    def __init__(self):
        self.users_storage = UsersStorage()

    def add_room(self, user, room):
        pass

    def delet_room(self, user, room):
        pass

