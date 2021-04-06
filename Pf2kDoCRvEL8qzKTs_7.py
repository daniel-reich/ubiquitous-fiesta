
def order_people(l,p):
  if l[0]*l[1] < p:
    return "overcrowded"
  x = [[i*l[1]+j+1 for j in range (l[1])] for i in range (l[0])]
  for i in range (l[0]):
    x[i].sort(reverse=(i%2==1))
  for i in range (l[0]):
    for j in range (l[1]):
      if x[i][j] > p:
        x[i][j] = 0
  return x

