
class Person:
  
  def __init__ (self,name,likes,hates):
    self.name = name
    self.likes = likes
    self.hates = hates
    
  def taste(self,food):
    if food in self.likes: add = " and loves it"
    elif food in self.hates: add = " and hates it"
    else: add=""
    return self.name + " eats the " + food + add + "!"

