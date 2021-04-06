
class Person:
  
  def __init__(self,person_name,like_list,hate_list):
    self.person_name = person_name
    self.like_list = like_list
    self.hate_list = hate_list
    
  def taste(self,food):
    for i in self.like_list:
      if food == i:
        return "{} eats the {} and loves it!".format(self.person_name,i)
    for j in self.hate_list:    
      if food == j:
        return "{} eats the {} and hates it!".format(self.person_name,j)
        
    else:
      return "{} eats the {}!".format(self.person_name, food)

