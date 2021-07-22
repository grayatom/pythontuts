# inheritence
class Employee:
    
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def raise_pay(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, p_lang):
        super().__init__(first, last, pay)
        self.p_lang = p_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())
            

dev_1 = Developer('ayush', 'prakash', 150000, 'python')
dev_2 = Developer('test', 'user', 100000, 'java')

mgr_1 = Manager('Sue', 'Big', 120000, [dev_1])

print(mgr_1.email)
mgr_1.add_employee(dev_2)
mgr_1.print_emps()
mgr_1.remove_employee(dev_2)
mgr_1.print_emps()
print(dev_1.email)
print(dev_1.p_lang)

