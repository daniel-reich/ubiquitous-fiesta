
def make_change(c):
  coins = [25,10,5,1]
  names = ['q','d','n','p']
  tot = 0
  i = 0
  res = {'q':0,'d':0,'n':0,'p':0}
  while tot < c:
    if tot + coins[i] > c:
      i += 1
    else:
      tot += coins[i]
      res[names[i]] += 1
  return res

