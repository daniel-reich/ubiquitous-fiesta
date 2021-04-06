
class Employee:
  def __init__(self, name, **attributes):
    self.firstname, self.lastname = name.split()
    for k, v in attributes.items():
      setattr(self, k, v)

