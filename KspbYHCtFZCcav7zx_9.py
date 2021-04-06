
def bill_split(spicy, cost):
  f = sum([x[1] for x in list(zip(spicy, cost)) if x[0] == 'N'])/2
  y = sum(cost) - f
  return [y,f]

