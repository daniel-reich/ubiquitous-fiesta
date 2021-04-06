
def bill_split(spicy, cost):
  mycost=0
  friendcost=0
  for i in range(0,len(spicy)):
    if spicy[i] == 'S':
      mycost += cost[i]
    elif spicy[i] == 'N':
      mycost += cost[i]/2
      friendcost += cost[i]/2
  return [mycost, friendcost]

