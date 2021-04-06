
def pirates_killed(gold, tolerance):
  maximum = max(gold)
  mylist = []
  for i in range (len(gold)):
    mylist.append(maximum-gold[i])
  for i in range (len(tolerance)):
    if (tolerance[i] < mylist[i]):
      return True
  return False

