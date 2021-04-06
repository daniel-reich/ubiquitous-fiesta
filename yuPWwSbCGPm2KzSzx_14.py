
prices = {
  "Strawberries" : "$1.50",
  "Banana" : "$0.50",
  "Mango" : "$2.50",
  "Blueberries" : "$1.00",
  "Raspberries" : "$1.00",
  "Apple" : "$1.75",
  "Pineapple" : "$3.50"
}
​
class Smoothie:
  def __init__(self, ingredients):
    self.ingredients= ingredients
  
  def get_cost(self):
    cost = 0
    for item in self.ingredients:
      cost+=float(prices[item][1:])
    return "${}".format(format(round(cost,2),'.2f'))
    
  def get_price(self):
    return "${}".format(format(round(float(self.get_cost()[1:])+float(self.get_cost()[1:])*1.5,2),'.2f'))
  
  def get_name(self):
    ingredients = self.ingredients.copy()
    ingredients.sort()
    for ind,item in enumerate(ingredients):
      ingredients[ind] = item.replace("berries" , "berry")
    if len(ingredients)>1:
      ingredients.append('Fusion')
    else:
      return "{} Smoothie".format(ingredients[0])
    string = ' '.join(ingredients)
    return string

