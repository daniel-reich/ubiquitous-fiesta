
def bill_split(spicy, cost):
  upay = sum([j for i,j in zip(spicy,cost) if i=="S"])
  fpay = round(sum([j for i,j in zip(spicy,cost) if i=="N"])/2)
  return [upay+fpay,fpay]

