# Stwórz klasę Animal, która ma atrybuty name i age, oraz metodę sound
# >>> animal = Animal("Strange something", 1000)
# >>> animal.name
# "Strange something"
# >>> animal.age
# 1000
# >>> animal.sound()
# "kncok kncok"
# Stwórz klasy Dog i Cat, które dziedziczą po Animal i przeciążają metodę sound tak, że:
# >>> cat = Cat("Albert", 5)
# >>> dog = Dog("Nina", 6)
# >>> dog.sound()
# "how how"
# >>> cat.sound()
# "... (sorry - that's cat!)"
# Przeciaż operator >  tak by, można było porównywać wiek:
# >>> cat > dog
# True
# >>> dog > animal
# False

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age

    def sound(self):
        pass


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(self, name, age)

    def sound(self):
        s = super(Animal).sound(self)
        s = '... (sorry - that\'s cat!)'
        return s


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(self, name, age)

    def sound(self):
        s = super(Animal).sound(self)
        s = 'how how'
        return s


def test_animal():
    animal = Animal("Strange something", 1000)
    assert animal.name == "Strange something"
