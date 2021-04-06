
class Person:
  def __init__(self,Name,lv_lst,ht_lst):
    self.name = Name
    self.lv_lst = lv_lst
    self.ht_lst = ht_lst
    
  def taste(self,food_name):
    self.food_name = food_name
    if self.food_name in self.lv_lst:
      return "{} eats the {} and loves it!".format(self.name, self.food_name)
    elif self.food_name in self.ht_lst:
      return "{} eats the {} and hates it!".format(self.name, self.food_name)
    else:
      return "{} eats the {}!".format(self.name,self.food_name)

