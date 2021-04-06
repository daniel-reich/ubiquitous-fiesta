
class Employee:
    def __init__(self, name, **attr):
      self.name, self.lastname = name.split()
      for k, v in attr.items():
        setattr(self, k, v)

