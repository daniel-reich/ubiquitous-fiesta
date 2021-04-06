
def sock_pairs(socks):
  return sum(socks.count(x)//2 for x in set(socks))

