
def add_bill(money):
  sum = 0
  for x in money.split(','):
    val = int(''.join([a for a in x if a.isdigit()]))
    if 'd' in x:
      if 'k' in x:
        sum += (val*1000)
      else:
        sum += val
  return sum

