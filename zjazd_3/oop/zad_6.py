class Produkt:

    def __init__(self, id, name, price, discount = 0):
        self.price = price

        self._id = id
        self._name = name
        self._discount = discount

    @property
    def full_name(self):
        return 'Produkt: ' + self._name

    @property
    def discount_price(self):
        return (self.price * self._discount) / 100

    @property
    def discount(self):
        ''' price after discount'''
        return self._discount

    @discount.setter
    def discount(self, user_value):
        if type(user_value) == int and 0 < user_value < 30:
            self._discount = user_value


    @discount.deleter
    def discount(self):
        self.discount = 0

    # ale musze mieć propoerty, które zwraca te wartość
    @property
    def name(self):
        return self._name

    # mogę nadpisać name pod jakimś warunkiem
    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value


def test_discount_ko():
    pr1 = Produkt(1, 'chleb', 10, 5)
    pr1.name = 'ko'
    assert pr1.name == 'chleb'


def test_discount_woda():
    pr1 = Produkt(1, 'chleb', 10, 5)
    pr1.name = 'woda'
    assert pr1.name == 'woda'


def test_discount_text():
    pr1 = Produkt(1, 'chleb', 10, 5)
    pr1.discount = 'dwsdfwr'
    assert pr1.discount == 5


def test_discount_50():
    pr1 = Produkt(1, 'chleb', 10, 5)
    pr1.discount = 50
    assert pr1.discount == 5


def test_discount_11():
    pr1 = Produkt(1, 'chleb', 10, 5)
    pr1.discount = 11
    assert pr1.discount == 11


def test_discount_11():
    pr1 = Produkt(1, 'chleb', 10, 5)
    pr1.discount = 10
    assert pr1.discount_price == 1.0

