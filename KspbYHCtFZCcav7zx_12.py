
def bill_split(spicy, cost):
  f = 0
  y = 0
  comb = zip(spicy, cost)
  for i in comb:
    if i[0] == 'S':
      y = y + i[1]
    else:
      y = y + i[1] / 2
      f = f + i[1] / 2
      
      
  return [y,f]

