
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
​
  def compare_age(self, other):
    if self.age > other.age:
      stmt = "younger than me"
    elif self.age < other.age:
      stmt =  "older than me"
    else:
      stmt = "the same age as me"
    return "{0} is {1}.".format(other.name, stmt)

