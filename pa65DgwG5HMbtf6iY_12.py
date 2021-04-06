
class player():
​
  def __init__(self, name, age, height, weight):
  # complete function
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
    
  def get_age(self):  
  # complete function
    return "%s is age %s" %(self.name, self.age)
  def get_height(self): 
  # complete function
    return "%s is %scm" %(self.name, self.height)
  def get_weight(self): 
  # complete function
    return "%s weighs %skg" %(self.name, self.weight)

