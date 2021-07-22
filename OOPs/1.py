class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last


e1 = Employee('ayush', 'prakash', 150000)
e2 = Employee('test', 'user', 100000)
print(e1.fullname())
print(e2.fullname())
