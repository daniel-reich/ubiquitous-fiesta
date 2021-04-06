
def make_sandwich(i, f):
  c = 0
  while c < len(i):
      if i[c] == f:
          i.insert(c,'bread')
          c+=2
          i.insert(c,'bread')
      else:
          c+=1 
  return i

