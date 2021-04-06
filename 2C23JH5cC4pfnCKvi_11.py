
def check_flush(table, hand):
  elems = sum([x.split('_') for x in table+hand],[])
  return any([elems.count(x)>=5 for x in set(elems)])

