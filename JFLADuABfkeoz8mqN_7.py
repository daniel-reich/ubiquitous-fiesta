
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
​
  def compare_age(self, other):
    x = " is older than me." if other.age > self.age else " is younger than me." if other.age < self.age else " is the same age as me."
    return other.name+x

