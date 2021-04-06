
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
    self.ingredients = ingredients[:]
    
  def get_cost(self):
    a = str(sum([float(prices.get(i)[1:]) for i in self.ingredients]))
    return "$" + a if len(a.split(".")[1]) == 2 else "$" + a + "0"
    
  def get_price(self):
    a = str(round(float(self.get_cost()[1:])*(1 + 1.5), 2))
    return "$" + a if len(a.split(".")[1]) == 2 else "$" + a + "0"
    
  def get_name(self):
    if len(self.ingredients) > 1:
      s = " ".join(sorted(self.ingredients))
      return s.replace("ries", "ry") + " Fusion"
    else:
      s = self.ingredients[0]
      return s.replace("ries", "ry") + " Smoothie"

