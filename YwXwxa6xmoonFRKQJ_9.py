
def josephus(n): 
  n = list(range(n))
  k = 0
  while len(n) > 1:
    m = len(n)
    n = n[k::2]     
    if m % 2 == 1:
      k += 1
    k %= 2
  else :
    return n[0] if n else False

