
class player():
  
  def __init__(self, name, age, height, weight):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
    
  def get_age(self):
      a = str(self.name)+" is age " +str(self.age)
      return a
    
  def get_height(self):
    b = str(self.name)+" is " +str(self.height)+"cm"
    return b
    
  def get_weight(self):
    c = str(self.name)+" weighs " +str(self.weight)+"kg"
    return c
​
p1 = player("Austun Louw", 20, 192,17)
print(p1.get_age())
print(p1.get_height)
print(p1.get_weight)

