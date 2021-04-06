
class Employee:
  def __init__(self, name, **kargs):
    self.__dict__ = kargs
    self.name, self.lastname = name.split(' ')

