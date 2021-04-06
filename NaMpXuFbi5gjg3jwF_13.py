
def sock_pairs(socks):
  sock = list(set(socks))
  count = 0
  for s in sock:
    count += socks.count(s)//2
  return count

