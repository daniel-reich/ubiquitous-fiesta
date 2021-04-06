
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def compare_age(self, other):
    txt = [
      'younger than', 
      'the same age as', 
      'older than'
      ][(self.age <= other.age) + (self.age < other.age)]
      
    return '{} is {} me.'.format(other.name, txt)

