
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
​
  def compare_age(self, other):
    if (other.age > self.age):
      return other.name + " is older than me."
    if (other.age < self.age):
      return other.name + " is younger than me."
    if (other.age == self.age):
      return other.name + " is the same age as me."

