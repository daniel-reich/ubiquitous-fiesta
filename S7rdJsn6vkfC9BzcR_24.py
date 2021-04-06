
class Employee:
  def __init__(self, name, **args):
    self.name=name.split(' ')[0]
    self.lastname=name.split(' ')[1]
    for key, value in args.items():
      self.__dict__[key] = value

