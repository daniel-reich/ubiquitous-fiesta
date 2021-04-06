
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
​
  def compare_age(self, other):
    comp = ['older than', 'younger than', 'the same age as']
    string = comp[0] if self.age < other.age else comp[1] if self.age > other.age else comp[2]
    return '{} is {} me.'.format(other.name, string)

