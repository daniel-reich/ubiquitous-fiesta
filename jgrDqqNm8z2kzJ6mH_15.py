
tax = 1.06 
def checkout(cart):
   return sum([amt(d) for d in cart])
​
def amt(d):
   x = d['prc'] * d['qty']
   if d['taxable']:
      x = x * tax
   return x

