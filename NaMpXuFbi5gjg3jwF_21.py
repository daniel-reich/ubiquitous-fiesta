
def sock_pairs(socks):
  return sum(socks.count(i)//2 for i in set(socks))

