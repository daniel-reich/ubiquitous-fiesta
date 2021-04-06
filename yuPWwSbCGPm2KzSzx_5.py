
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
  def __init__(self, ing):
    self.ingredients = ing
  
  def get_cost(self):
    return '${:.2f}'.format(sum(float(prices[i][1:]) for i in self.ingredients))
  
  def get_price(self):
    return '${:.2f}'.format(float(self.get_cost()[1:]) * 2.5)
  
  def get_name(self):
    ings = sorted(i.replace('ries','ry') for i in self.ingredients)
    return ings[0] + ' Smoothie' if len(ings)==1 else ' '.join(ings) + ' Fusion'

