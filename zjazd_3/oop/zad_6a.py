import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'V({self.x}, {self.y}): {self.length}'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        v_ret = Vector(new_x, new_y)
        return v_ret

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        v_ret = Vector(new_x, new_y)
        return v_ret

    def __mul__(self, other):
        new_x = self.x * other
        new_y = self.y * other
        v_ret = Vector(new_x, new_y)
        return v_ret

    def __eq__(self, other):
        return self.length == other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length


    def __ne__(self, other):
        return self.length != other.length



    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


def test_wektor():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=3, y=4)
    vector3 = vector_1 + vector_2
    assert vector3.x == 4
    assert vector3.y == 6


def test_wektor_odejmowanie():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=3, y=4)
    vector3 = vector_1 - vector_2
    assert vector3.x == -2
    assert vector3.y == -2


def test_wektor_mnozenie():
    vector_1 = Vector(x=1, y=2)
    liczba = 4
    vector3 = vector_1 * liczba
    assert vector3.x == 4
    assert vector3.y == 8


def test_wektor_dlugosc():
    vector_1 = Vector(x=3, y=4)
    assert vector_1.length == 5


def test_wektor_equal():
    vector_1 = Vector(x=3, y=4)
    vector_2 = Vector(x=3, y=4)
    assert vector_1 == vector_2


def test_wektor_equal_2():
    vector_1 = Vector(x=3, y=4)
    vector_2 = Vector(x=-3, y=-4)
    assert vector_1 == vector_2


def test_wektor_greater_than():
    vector_1 = Vector(x=3, y=4)
    vector_2 = Vector(x=1, y=1)
    assert vector_1 > vector_2


def test_wektor_greater_than_or_equal():
    vector_1 = Vector(x=3, y=4)
    vector_2 = Vector(x=1, y=1)
    assert vector_1 >= vector_2


def test_wektor_lower_than():
    vector_2 = Vector(x=3, y=4)
    vector_1 = Vector(x=1, y=1)
    assert vector_1 < vector_2


def test_wektor_lower_than_or_equal():
    vector_2 = Vector(x=3, y=4)
    vector_1 = Vector(x=1, y=1)
    assert vector_1 <= vector_2

def test_wektor_equal_ne():
    vector_1 = Vector(x=3, y=4)
    vector_2 = Vector(x=-1, y=-1)
    assert not vector_1 == vector_2


def test_wektor_equal_3_wektory():
    vector_1 = Vector(x=3, y=4)
    vector_2 = Vector(x=-1, y=-1)
    vector_3 = Vector(x=-2, y=2)
    lista = [vector_1, vector_2, vector_3]
    assert sorted(lista) == [vector_2, vector_3, vector_1]
    for item in lista:
        print(item)
