
def sock_pairs(socks):
  a = [socks.count(i) for i in set(socks)]
  return sum([int(i/2) for i in a if i>1])

