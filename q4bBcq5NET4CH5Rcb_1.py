
def jay_and_bob(t):
  n=round(14/{'q':2,'e':4,'s':8}.get(t[0],1),2)
  return'%s grams'%(n%1and n or int(n))

