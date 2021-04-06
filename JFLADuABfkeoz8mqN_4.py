
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def compare_age(self, other):
    if other.age > self.age: adj = "older than"
    elif other.age == self.age: adj = "the same age as"
    else: adj = "younger than"
    return "{} is {} me.".format(other.name, adj)

