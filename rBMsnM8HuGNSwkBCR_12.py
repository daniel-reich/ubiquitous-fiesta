
def add_bill(money):
  m=money.split(',')
  sume=0
  for i in m:
    if 'd' in i:
      if 'k' in i:
        sume+=int(i[1:-1])*1000
      else:
        sume+=int(i[1:])
  return sume

