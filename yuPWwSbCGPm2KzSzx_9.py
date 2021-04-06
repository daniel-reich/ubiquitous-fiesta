
tprices = {
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
  def __init__(self,ingredients):
    self.ingredients = ingredients
  def get_cost(self):
    return '${:.2f}'.format(sum(float(tprices[i][1:]) for i in self.ingredients))
  def get_price(self):
    return '${:.2f}'.format(float(self.get_cost()[1:])+float(self.get_cost()[1:])*1.5)
  def get_name(self):
    fruits = sorted(self.ingredients)
    for i in range(len(fruits)):
      fruits[i] = fruits[i].replace('berries','berry')
    return ' '.join(fruits)+(' Smoothie' if len(fruits)==1 else ' Fusion')

