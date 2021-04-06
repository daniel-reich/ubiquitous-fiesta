
def get_total_price(groceries):
  myans = 0
  for i in range(len(groceries)):
    myans += groceries[i]['quantity']*groceries[i]['price']
  return round(myans,10)

