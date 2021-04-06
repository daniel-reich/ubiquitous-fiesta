
class Employee:
​
    def __init__(self, str_names, **kwargs):
        _name, _lastname = str_names.split()
        self.name = _name
        self.lastname = _lastname
        for key, val in kwargs.items():
            setattr(self, key, val)

