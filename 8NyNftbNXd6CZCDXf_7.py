
def get_coin_balances(a, b):
  x, y = 3, 3
  for i in range(0, len(a)):
    x-=1
    y-=1
    if a[i]=='share':
      y+=3
    else:
      x+=1
    if b[i]=='share':
      x+=3
    else:
      y+=1
  return [x,y]

