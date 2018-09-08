class Employee():
    def __init__(self, name, last_name, wage):
        self.name = name
        self.last_name = last_name
        self.wage = wage

    def register_time(self, time):
        self.time = time
        if self.time > 24:
            raise Exception('DŁUŻEJ NIŻ DOBA!')
        else:
            return time

    def pay_salary(self):
        if self.time <= 8:
            return self.wage * self.time
        if self.time > 8:
            extra_time = self.time - 8
            return extra_time * 2 * self.wage + 8 * self.wage


def test_employee():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.name == 'Jan'
    assert employee.last_name == 'Nowak'
    assert employee.wage == 100.00


def test_register_time():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.register_time(5) == 5

#
# def test_register_time_overdue():
#     employee = Employee('Jan', 'Nowak', 100.0)
#
#     with


def test_pay_salary_5():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(0)
    assert employee.pay_salary() == 0.0


def test_pay_salary_10():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    assert employee.pay_salary() == 1200.0


def test_pay_salary_11():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(11)
    assert employee.pay_salary() == 1400.0
