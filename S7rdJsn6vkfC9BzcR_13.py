
class Employee:
  def __init__(self, fullname, **kwargs):
    self.name, self.lastname = fullname.split()
    for k, v in kwargs.items():
      setattr(self, k, v)

