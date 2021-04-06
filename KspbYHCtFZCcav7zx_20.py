
def bill_split(spicy, cost):
  you = 0
  fren = 0
  for i in range(len(spicy)):
    if spicy[i] == 'S':
      you += cost[i]
    else:
      you += cost[i]/2
      fren += cost[i]/2
  return [you,fren]

