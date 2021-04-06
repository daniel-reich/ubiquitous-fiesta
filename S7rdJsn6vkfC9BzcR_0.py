
class Employee:
    
    def __init__(self, full_name, **kwargs):
        self.full_name = full_name
        self.name, self.lastname = full_name.split()
        self.__dict__.update(kwargs)

