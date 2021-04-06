
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
​
  def compare_age(self, other):
    # Write code here!
    if self.age > other.age:
      return other.name + " is younger than me."
    elif self.age < other.age:
      return other.name + " is older than me."
    else:
      return other.name + " is the same age as me."

