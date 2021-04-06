
def sock_pairs(socks):
  p=0
  for i in socks:
    if socks.count(i)//2>=1:
      p+=socks.count(i)//2
      socks=socks.replace(i, '')
  return p

