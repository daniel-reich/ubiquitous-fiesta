
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
  # Write code here!
  def __init__(self,ingredients):
    self.ingredients = ingredients
​
  def get_cost(self):
    cost = sum(list(map(lambda x: float(prices[x][1::]),self.ingredients)))
    if str(cost)[-2] == ".":
      return "${}0".format(str(cost))
    else:
      return "${}".format(str(cost))
  def get_price(self):
    new_cost = round((float(self.get_cost()[1::]) + (float(self.get_cost()[1::]) * 1.5)),2)
    if str(new_cost)[-2] == ".":
      return "${}0".format(str(new_cost))
    else:
      return "${}".format(str(new_cost))
  def new_name(self,name):
    if name.endswith("ies"):
      return name[:-3] + "y"
    else:
      return name
  def get_name(self):
    if len(self.ingredients) == 1:
      smoothie = "Smoothie"
    else:
      smoothie = "Fusion"
    self.ingredients.sort()
    names = list(map(lambda x: self.new_name(x) + " ",self.ingredients))
    return ''.join(names) + smoothie

