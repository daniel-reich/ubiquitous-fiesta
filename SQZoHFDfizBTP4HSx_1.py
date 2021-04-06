
def missing_alphabets(t):
  d=[(t.count(x),x)for x in map(chr,range(97,123))]
  return''.join(k*(max(d)[0]-v)for v,k in d)

