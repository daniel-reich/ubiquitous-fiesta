
def sock_pairs(socks):
  pairs = [socks.count(i)//2 for i in set(socks) if socks.count(i) >= 2]
  return sum(pairs)

