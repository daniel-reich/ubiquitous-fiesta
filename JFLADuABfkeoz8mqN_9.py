
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
​
  def compare_age(self, other):
    if self.age > other.age:
      x = "younger than"
    elif self.age == other.age:
      x = "the same age as"
    else:
      x = "older than"
    return "{} is {} me.".format(other.name,x)

