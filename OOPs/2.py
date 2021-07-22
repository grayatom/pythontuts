# a class variable(raise percent) can be 
# accessed from both the class and the intance
# i prefer class : ) 
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



Employee.raise_percent = 1.07

e1 = Employee('ayush', 'prakash', 150000)
e2 = Employee('test', 'user', 100000)
e3 = Employee('test', 'user2', 120000)
print(Employee.num_employes)

