
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
class Smoothie(object):
    
    def __init__(self,ingredients):
        self.ingredients = ingredients
        self.cost = 0
        
    
    def get_cost(self):
        for i in self.ingredients:
            self.cost += float(prices[i][1:])
        self.cost = '{:.2f}'.format(self.cost)
        return '$'+self.cost
    
    def get_price(self):
        return '${:.2f}'.format(2.5*float(self.cost))
    
    def get_name(self):
        if len(self.ingredients) == 1:
            return ''.join(self.ingredients).replace('ies','y') + ' Smoothie'
        else:
            self.ingredients.sort()
            return ' '.join(self.ingredients).replace('ies','y')+' Fusion'

