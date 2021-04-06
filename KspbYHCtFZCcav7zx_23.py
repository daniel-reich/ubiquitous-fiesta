
def bill_split(spicy, cost):
  split = sum([y/2 for x,y in zip(spicy,cost) if x is 'N'])
  return [sum(cost) - split, split]

