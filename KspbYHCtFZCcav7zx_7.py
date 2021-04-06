
def bill_split(spicy, cost):
  return [sum(cost[i] if spicy[i] == 'S' else (cost[i] / 2) for i in range(len(cost))), sum(cost[i] / 2 for i in range(len(cost)) if spicy[i] == 'N')]

