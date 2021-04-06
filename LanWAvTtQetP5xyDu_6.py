
def coins_div(lst):
  if sum(lst)%3: return False
  dtbs = {(0,0,0)} #set of possible distributions with inital subset of coins
  coor = [0,1,2]
  for cn in lst:
    dtbs = dtbs.union({tuple(d[i]+cn*(i==j) for i in coor) for j in coor for d in dtbs})
  m=sum(lst)//3
  return (m,m,m) in dtbs

