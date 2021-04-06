
class CoffeeShop:
  def __init__(self,*l):self.n,self.m,self.o=l
  def add_order(self,d):
    if d in[x['item']for x in self.m]:self.o.append(d);return'Order added!'
    return'This item is currently unavailable!'
  fulfill_order=lambda self:self.o and'The %s is ready!'%self.o.pop(0)or'All orders have been fulfilled!'
  list_orders=lambda self:self.o
  due_amount=lambda self:round(sum(y['price']for y in self.m for x in self.o if x==y['item']),2)
  cheapest_item=lambda self:min(self.m,key=lambda x:x['price'])['item']
  drinks_only=lambda self:[x['item']for x in self.m if'drink'==x['type']]
  food_only=lambda self:[x['item']for x in self.m if'food'==x['type']]

