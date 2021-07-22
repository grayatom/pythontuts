# regular methods (takes the instance as arg)
# class methods (takes class as arg) 
# static methods (takes nothing as arg, but is logically
#                 related to the class so we write it in the class)
import datetime

class Employee:
    
    raise_percent = 1.04
    num_employes = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_employes += 1

    def fullname(self):
        return self.first + ' ' + self.last

    def raise_pay(self):
        self.pay = int(self.pay * Employee.raise_percent)
    
    @classmethod
    def set_raise_amt(cls, percent):
        cls.raise_percent = percent

    # class methods as alternative constructors
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    

e1 = Employee('ayush', 'prakash', 150000)
e2 = Employee('test', 'user', 100000)
my_date = datetime.date(2021, 7, 18)
if Employee.is_workday(my_date):
    print('Its a workday')
else:
    print('Its a weekend !!! enjoy : )')



