class ElectricCar():

    def __init__(self, range):
        self.range = range
        self.max = range


    def drive(self, distance):
        self.distance = distance
        if self.distance <= self.range:
            rest_range = self.range - distance
            self.range = rest_range
            return self.range
        else:
            return 0

    def charge(self):
        self.range = self.max
        return self.range


def test_car():
    car = ElectricCar(100)
    assert car.range == 100
    car1 = ElectricCar(50)
    assert car1.range <= 100


def test_drive():
    car = ElectricCar(100)
    assert car.drive(70) == 30
    assert car.drive(50) == 0
    assert car.drive(50) == 0
    car.charge()
    car.charge()
    assert car.drive(50) == 50
    assert car.drive(50) == 0
