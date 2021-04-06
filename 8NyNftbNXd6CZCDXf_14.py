
def get_coin_balances(lst1, lst2):
  x,y=3,3
  for i,j in zip(lst1,lst2):
    if i==j=="share":
      x+=2
      y+=2
    elif i!=j:
      if i=="share":
        x-=1
        y+=3
      else:
        x+=3
        y-=1
  return [x,y]

