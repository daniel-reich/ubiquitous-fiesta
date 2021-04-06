
class Stock:
  
  def __init__(self, prices):
    self.p = prices
​
class Wallet:
  
  def __init__(self):
    self.withdrawal = 0
    self.deposit = 0
  
  def buy(self, stock, day):
    self.withdrawal += stock.p[day]
    return True
  
  def sell(self, stock, day):
    self.deposit += stock.p[day]
    return True
  
  def difference(self):
    return self.deposit - self.withdrawal
  
  def refresh(self):
    self.deposit, self.withdrawal = [0, 0]
    return True
​
def stock_picker(lst):
  if list(reversed(sorted(lst))) == lst:
    return -1
  else:
    stock = Stock(lst)
    bank = Wallet()
    #print(stock.p)
    potential_profits = []
    
    
    for num in range(len(lst)):
      for n in range(num, len(lst)):
        buy_price = lst[num]
        sell_price = lst[n]
        
    #   print(buy_price, sell_price)
        
        bank.buy(stock, num)
        bank.sell(stock, n)
    #   print(bank.withdrawal, bank.deposit, bank.difference(), 'h')
        potential_profits.append(bank.difference())
    #   print(potential_profits)
        bank.refresh()
    #   print(bank.withdrawal, bank.deposit, bank.difference(), 'i')
    
    return max(potential_profits)

