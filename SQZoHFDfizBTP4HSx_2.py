
def missing_alphabets(t):
  d={x:t.count(x)for x in'abcdefghijklmnopqrstuvwxyz'}
  m=max(d.values())
  return''.join(sorted(k*(m-v)for k,v in d.items()))

