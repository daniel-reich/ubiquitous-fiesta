
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
​
  def compare_age(self, other):
    modifier = ''
    
    if self.age < other.age:
      modifier = 'older than'
    elif self.age == other.age:
      modifier = 'the same age as'
    else:
      modifier = 'younger than'
    
    return '{n} is {m} me.'.format(n = other.name, m = modifier)

