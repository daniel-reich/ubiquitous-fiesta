
def bill_split(spicy, cost):
  return [int(sum(cost[i] if spicy[i]=="S" else cost[i]/2 for i in range(len(spicy)))), int(sum(cost[i]/2 for i in range(len(spicy)) if spicy[i]=="N"))]

