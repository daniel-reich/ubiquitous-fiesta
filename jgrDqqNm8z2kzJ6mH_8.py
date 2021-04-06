
tax = .06
def checkout(cart):
  
  till = 0
  
  for item in cart:
    item_price = item['prc']
    item_quant = item['qty']
    item_tax = item['taxable']
    
    t = item_price * item_quant
    
    if item_tax == True:
      t += (t * tax)
    
    till += t
  
  return till

