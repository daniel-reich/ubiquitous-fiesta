
class Smoothie:
  prices = {
    "Strawberries" : "$1.50",
    "Banana" : "$0.50",
    "Mango" : "$2.50",
    "Blueberries" : "$1.00",
    "Raspberries" : "$1.00",
    "Apple" : "$1.75",
    "Pineapple" : "$3.50"
  }
  def __init__(self,ingredients):
    self.ingredients = ingredients
  
  def get_cost(self):
    tot_cost = 0
    for ingredient in self.ingredients:
      tot_cost += float(Smoothie.prices[ingredient][1:])
    return '${:.2f}'.format(tot_cost)
  
  def get_price(self):
     return '${:.2f}'.format(round(float(self.get_cost()[1:]) + 1.5*float(self.get_cost()[1:]), 2))
     
  def get_name(self):
    my_ingredients = sorted(self.ingredients)
    def change_name(names):
      new_lst = []
      for name in names:
        if 'rries' in name:
          new_lst.append(name.replace('rries', 'rry'))
        else:
          new_lst.append(name)
      return new_lst
    my_ingredients = change_name(my_ingredients)
    if len(my_ingredients) == 1:
      name = my_ingredients[0] + ' Smoothie'
    else:
      name = ''
      for ingredient in my_ingredients:
        name += ingredient + ' '
      name += 'Fusion'
    return name

