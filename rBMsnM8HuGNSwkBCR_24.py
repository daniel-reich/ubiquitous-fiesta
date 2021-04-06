
def add_bill(money):
  return sum(list([int(x.replace('d','').replace('k',''))*1000 if 'd' in x and 'k' in x else int(x.replace('d','')) for x in list([x for x in list([x for x in money.split(',')]) if 'd' in x])]))

