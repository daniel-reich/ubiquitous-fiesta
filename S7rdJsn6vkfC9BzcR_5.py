
class Employee:
  def __init__(self, name, **kwargs):
    self.firstname, self.lastname = name.split()
    for k, v in kwargs.items():
      if type(v) is str: v = '"{}"'.format(v)
      exec('self.{} = {}'.format(k, v))

