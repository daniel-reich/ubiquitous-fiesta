
class Smoothie:
​
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
  def __init__(self, ingredients):
    self.ingredients = ingredients
  
  def get_cost(self):
    return '${:0.2f}'.format(sum(float(Smoothie.prices.get(i).lstrip('$')) for i in self.ingredients))
    
  def get_price(self):
    return '${:0.2f}'.format(float(Smoothie.get_cost(self).lstrip('$')) * 2.5)
    
  def get_name(self):
    if len(self.ingredients) > 1:
      return ' '.join(sorted(self.ingredients)).replace('berries', 'berry') + ' Fusion'
    return self.ingredients[0].replace('berries', 'berry') + ' Smoothie'

