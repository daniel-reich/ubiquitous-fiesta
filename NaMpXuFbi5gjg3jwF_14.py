
def sock_pairs(socks):
  return sum([n // 2 for n in [socks.count(ch) for ch in set(socks)]])

