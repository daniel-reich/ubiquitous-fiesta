
def divide(x, y):
  print(x, y)
  if x == 0 or abs(x) < abs(y):
    return 0
  else:
    if [x>0,y>0] == [True,True] or [x>0,y>0] == [False,False]:
      return 1 + divide(x-y, y)
    else:
      tr = -1 + divide(x + y, y)
      return tr

