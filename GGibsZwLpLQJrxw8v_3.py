
def get_lucky_number(size, nth):
  n = [x for x in range(1,size+1)]
  c = 1
  for x in range(1,len(n)+1):
    s = n[c]
    l = n[n[c]-1::n[c]]
    if l:
      for i in l: n.pop(n.index(i))
      if s in n:  c+=1
    else: break
  return n[nth-1]

