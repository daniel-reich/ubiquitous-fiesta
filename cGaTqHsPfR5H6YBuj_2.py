
def make_sandwich(i,f):
  for x in range(len(i)-1,-1,-1):
    if i[x] == f:
      i.insert(x+1, 'bread')
      i.insert(x,'bread')
  return i

