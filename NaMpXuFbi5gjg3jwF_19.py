
def sock_pairs(socks):
  l=[x for x in socks]
  l1=set(sorted(l))
  cnt=0
  for x in l1:
    cnt+=l.count(x)//2
  return cnt

