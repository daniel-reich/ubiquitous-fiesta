
def lemonade(bills):
​
  class Stand:
​
    def __init__(self, price):
      self.p = price
      self.bills = []
    
    def buy(self, bill):
      if bill < self.p:
        return False
      elif bill == self.p:
        self.bills.append(bill)
        return True
      else:
        change = bill - self.p
        possible_payments = []
​
        if change == 5:
          possible_payments = [[5]]
        elif change == 10:
          possible_payments = [[5, 5], [10]]
        else:
          possible_payments = [[5, 5, 5], [10, 5]]
        
        for possability in possible_payments:
          valid = True
          for bll in set(possability):
            if bll not in self.bills:
              valid = False
              break
            bill_count = self.bills.count(bll)
            poss_count = possability.count(bll)
​
            if bill_count < poss_count:
              valid = False
              break
          if valid == True:
            for bll in possability:
              try:
                self.bills.pop(self.bills.index(bll))
              except ValueError:
                return possability, self.bills, change
            self.bills.append(bill)
            return True
        self.bills.append(bill)
        return False
​
  stand = Stand(5)
​
  for bill in bills:
    purchase = stand.buy(bill)
   # print(stand.bills)
    if purchase == False:
      return False
    elif isinstance(purchase, bool) == False:
      return purchase
  
  return True

