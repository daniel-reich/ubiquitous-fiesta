
def sock_pairs(socks):
  return sum( socks.count(st)//2 for st in set(socks) )

