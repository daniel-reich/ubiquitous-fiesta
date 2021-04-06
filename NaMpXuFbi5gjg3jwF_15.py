
def sock_pairs(socks):
  total = 0
  for sock in set(socks):
    x = socks.count(sock)
    if x>1:
      total += x//2 
  return total

