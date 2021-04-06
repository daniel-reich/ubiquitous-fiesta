
def add_bill(money):
  s = 0
  for i in money.split(','):
    if i.startswith('d'):
      if i.endswith('k'):
        s+=int(i[1:-1])*1000
      else:
        s+=int(i[1:])
  return s

