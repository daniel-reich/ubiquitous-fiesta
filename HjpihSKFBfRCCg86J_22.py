
def compound_interest(p, t, r, n):
   amount = p*(1 + r/n)**(n*t)
   return round (amount, 2)

