
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
  def __init__(self,ing):
    self.ingredients=ing;
    
  def get_cost(self):   
    total = 0
    for i in self.ingredients:
      price = prices[i][1:]
      p = float(price)
      total += p
    return '${:.2f}'.format(total)
  
  def get_price(self):
    price = self.get_cost()
    p = float(price[1:])
    p2 = round(p + 1.5 * p,2)
    return '${:.2f}'.format(p2)
  
  def get_name(self):
    lst = []
    for item in self.ingredients:
      lst.append(item.replace('berries','berry'))
    lst.sort()
    final=''
    for item in lst:
      final = final + item + ' '
    if len(lst)==1:
      final += 'Smoothie'
    else:
      final += 'Fusion'
    return final

