
class Employee:
  def __init__(self, fullname, **kwargs):
    self.name, self.lastname = fullname.split(' ')
    for key, value in kwargs.items():
      setattr(self, key, value)

