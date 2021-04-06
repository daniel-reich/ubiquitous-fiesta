
def vending_machine(products, money, product_number):
  try:p = next(p for p in products if p['number']==product_number)
  except:return 'Enter a valid product number'
  r = money-p['price']
  change = []
  c = [500, 200, 100, 50, 20, 10]
  i=0
  while i<len(c):
    if r>=c[i]:
      change.append(c[i])
      r-=c[i]
    else:
      i+=1
  if change or r==0:
    return {'product':p['name'], 'change':change}
  return 'Not enough money for this product'

