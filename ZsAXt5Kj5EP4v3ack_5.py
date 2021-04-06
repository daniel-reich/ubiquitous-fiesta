
def secret(txt):
  n=int(txt[-1])
  c=txt.count('$')
  k=txt.find('$')
  d=txt.find('.')
  u=txt.find('>')
  A=[txt[d+1:k]+str(i).zfill(c) for i in range(1, n+1)]
  B=["<{0} class='{1}'></{0}>".format(txt[u+1:d], x) for x in A]
  return '<{0}>{1}</{0}>'.format(txt[:u], ''.join(B))

