
class Employee:
    def __init__(self, fullName, **kwargs):
        self.firstname, self.lastname = fullName.split()
        self.__dict__.update(kwargs)

