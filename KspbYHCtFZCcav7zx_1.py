
def bill_split(spicy, cost):
  s = sum(y for (x,y) in zip(spicy,cost) if x=='S')
  n = (sum(cost)-s)
  return [n/2+s,n/2]

