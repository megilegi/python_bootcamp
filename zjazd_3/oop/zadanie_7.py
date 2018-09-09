from zjazd_3.oop.zad_2 import Employee


class PremiumEmployee(Employee):

    def __init__(self, name, last_name, wage, bonus=0):
        super().__init__(name, last_name, wage)
        self.bonus = bonus

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        sal = super(PremiumEmployee, self).pay_salary()
        sal += self.bonus
        self.bonus = 0
        return sal

    @classmethod
    def create_hero(cls):
        return PremiumEmployee('pracownik', 'miesiac', 0, 0)


#tworzymy employa na podstawie stringa, parametry porozdzielany średnikami
    @classmethod
    def emp_from_string(cls, napis):
        list_param = napis.split(';')
        return PremiumEmployee(list_param[0], list_param[1], list_param[2])


    @staticmethod
    def say_hello():
        return 'Hello'


def test_employee():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    assert employee.name == 'Jan'
    assert employee.last_name == 'Nowak'
    assert employee.wage == 100.00
    assert employee.bonus == 0


def test_register():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000)
    employee.give_bonus(400)
    assert employee.bonus == 1400
    assert employee.pay_salary() == 1900


def test_employee_of_the_month():
    employee = PremiumEmployee.create_hero()
    assert employee.pay_salary() == 0

def test_imort_from_text():
    param = 'Henryk;Zdun;50'
    employee = PremiumEmployee.emp_from_string(param)
    assert employee.name == 'Henryk'
    assert  employee.last_name == 'Zdun'
