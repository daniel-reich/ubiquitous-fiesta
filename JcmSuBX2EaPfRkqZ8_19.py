
def get_total_price(groceries):
  tot=0
  for d in groceries:
    tot+=d['quantity']*d['price']
  return round(tot,1)

