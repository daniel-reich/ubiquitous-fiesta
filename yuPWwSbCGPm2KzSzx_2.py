
prices={"Strawberries":1.5,"Banana":.5,"Mango":2.5,"Blueberries":1,"Raspberries":1,"Apple":1.75,"Pineapple":3.5}
class Smoothie:
  def __init__(self,l):self.i=self.ingredients=l[:]
  __cost=lambda self:sum(prices[x]for x in self.ingredients)
  get_cost=lambda self:'$%.2f'%self.__cost()
  get_price=lambda self:'$%.2f'%(self.__cost()*2.5)
  def get_name(self):
    l=[x if x[-1]!='s'else x.rstrip('ies')+'y'for x in sorted(self.i)]
    return' '.join(l)+(' Fusion'if len(l)>1else' Smoothie')

