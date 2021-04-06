
def sock_merchant(socks):
  matches = 0
  for sock in set(socks):
    count = socks.count(sock)
    if count >= 2:
      matches += count // 2
  return matches

