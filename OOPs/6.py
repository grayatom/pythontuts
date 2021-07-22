# property decorators

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first + '.' + self.last + '@company.com'

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('deleted!!!')
        self.first = None
        self.last = None

e1 = Employee('ayush', 'prakash')
e1.fullname = 'Ayush Prkash'
# e1.first = 'aayush'
print(e1.email)
del e1.fullname



