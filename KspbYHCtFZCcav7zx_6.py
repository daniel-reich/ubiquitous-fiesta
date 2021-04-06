
def bill_split(spicy, cost):
  r=[0,0]
  for c in range(len(spicy)):
    if spicy[c]=='S':
      r[0]+=cost[c]
    else:
      r[1]+=cost[c]/2
      r[0]+=cost[c]/2
  return [int(c) for c in r]

