
def bill_split(spicy, cost):
  s, ns = 0, 0
  for i in range(len(spicy)):
    if spicy[i]=='S':
      s += cost[i]
    else:
      ns += cost[i]
      
  return [s+ns//2, ns//2]

