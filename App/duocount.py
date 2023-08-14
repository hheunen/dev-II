from user import User

class Duocount:
    def __init__(self,name):
        self.__name = name
        self.__users = []

    @property
    def users(self):
        return self.__users
    
    @property
    def name(self):
        return self.__name

    @users.setter
    def users(self, new_users):
        self.__users = new_users

    @property
    def due(self):
        return self.__due

    @due.setter
    def due(self, new_due):
        self.__due = new_due

    def add_user(self, username):
        self.__users.append(User(username))
    
    def user_in(self,username):
        for user in self.users:
            if username == user.name:
                return True
        return False

    def add_expense(self,username,price,liste_username):
        number_user=len(liste_username)
        print(price,' ea ', number_user)
        price=int(price)/number_user
        for user in self.users:
            if user.name == username:
                user.money+=price*(number_user-1)
            elif user.name in liste_username:
                user.money-=price


    def __repr__(self):
        name="Voici le duocount famille\n"
        user=""
        for username in self.users:
            user+=username.name +'\n'
        return name + user