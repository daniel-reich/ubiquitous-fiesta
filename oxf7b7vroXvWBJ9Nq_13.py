
def discount(n, txt):
  discount_lst = txt.split(', ')
  discount_lst = sorted(discount_lst, key=lambda x: x.endswith('%'), reverse=True)
  for discount in discount_lst:
    if discount.endswith('%'):
      n -= n*float(discount.strip('%'))/100
    elif discount == '':
      continue
    else:
      n -= float(discount)
  
  n = round(n,2)
  if str(n).endswith('.0'):
    return int(n)
  else:
    return n

