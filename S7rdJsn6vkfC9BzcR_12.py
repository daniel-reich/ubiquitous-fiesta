
class Employee:
  def __init__(self, FullName, **kwargs):
    self.firstname, self.lastname = FullName.split(" ")
    for arg in kwargs:
      setattr(self, arg, kwargs[arg])

