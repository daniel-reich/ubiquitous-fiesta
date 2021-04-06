
def sock_pairs(socks):
  lst=list(socks)
  set1=list(set(list(socks)))
  pairs=0
  for i in set1:
    if lst.count(i)>1:
      pairs=pairs+lst.count(i)//2
  return pairs

