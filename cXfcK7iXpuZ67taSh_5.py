
def mystery_func(txt):
  a = [i for i in txt if i.isalpha()]
  d = [i for i in txt if i.isnumeric()]
  return ''.join(i*int(j) for i,j in zip(a,d))

