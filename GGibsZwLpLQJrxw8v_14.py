
def get_lucky_number(size, nth):
  l = list(range(1,size+1))
  i = 1
  while len(l) > i:
    i += 1
    if i in l:
      l = list(filter(lambda x: (l.index(x)+1) % i, l))
      
  return l[nth-1]

