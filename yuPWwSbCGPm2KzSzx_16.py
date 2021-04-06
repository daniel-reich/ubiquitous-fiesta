
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
    self.ingredients=ingredients
  
  def get_cost(self):
    cost=0
    for i in self.ingredients: cost+=float(prices[i][1:])
    return "$"+'{:.2f}'.format(cost)
    
  def get_price(self):
    return "$"+'{:.2f}'.format(float(self.get_cost()[1:])*2.5)
​
  def get_name(self):
    a=""
    self.ingredients.sort()
    
    if len(self.ingredients) == 1:
      a = self.ingredients[0].replace("ies","y") + " Smoothie"
    
    else:
      for i in self.ingredients:
        a+=i.replace("ies","y")+" "
      a+="Fusion"
    return a

