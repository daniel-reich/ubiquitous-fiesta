
class Employee(object):
    def __init__(self, fullname, **kwargs):
        names = fullname.split(' ')
        self.name = names[0]
        self.lastname = names[1]
        self.__dict__.update(kwargs)

