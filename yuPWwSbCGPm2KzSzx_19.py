
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
​
class Smoothie:
  def __init__(self, ingredients):
    self.ingredients = ingredients
  
  def get_cost(self):
    cost = sum(
      float(prices[ingredient][1:])
      for ingredient in self.ingredients)
    return '${:.2f}'.format(cost)
  
  def get_price(self):
    cost = float(self.get_cost()[1:])
    price = cost + cost * 1.5
    return '${:.2f}'.format(price)
    
  def get_name(self):
    ingredients = sorted(
      ingredient.replace('berries', 'berry')
      for ingredient in self.ingredients)
    smoothie_type = 'Fusion' if len(self.ingredients) > 1 else 'Smoothie'
    return '{} {}'.format(' '.join(ingredients), smoothie_type)

