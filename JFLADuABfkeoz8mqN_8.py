
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
​
  def compare_age(self, other):
    if self.age<other.age:
      return "{} is older than me.".format(other.name)
    elif self.age>other.age:
      return "{} is younger than me.".format(other.name)
    else:
      return '{} is the same age as me.'.format(other.name)

