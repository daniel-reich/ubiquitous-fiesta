
def sock_pairs(socks):
  pairs=0
  nn=0
  for i in socks:
    if socks.index(i,nn)==0:
      pairs=pairs+socks.count(i)/2-.5*(socks.count(i)%2)
    else:
      if socks.index(i,0)==socks.index(i,nn):
        pairs=pairs+socks.count(i)/2-.5*(socks.count(i)%2)
    nn+=1
  return pairs

