class User:
    def __init__(self, name,money=0):
        self.__name = name
        self.__money = money

    @property
    def name(self):
        return self.__name
    
    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, new_money):
        self.__money = new_money


    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __repr__(self):
        return self.name + ' a '  + str(self.money) + " euros."