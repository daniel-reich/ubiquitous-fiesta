
def combo(lst, n):
  from itertools import combinations as c
  rawtr = list(c(lst, n))
  
  tr = []
  for item in rawtr:
    l = []
    for num in item:
      l.append(num)
    tr.append(l)
    
  return tr

