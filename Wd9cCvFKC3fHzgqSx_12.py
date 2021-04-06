
def num_split(num):
  i=0
  ls = []
  n = abs(num)
  while n!=0:
    mod = n%10
    pv = mod*(10**i)
    n = n//10
    if num<0:
      ls.insert(0,-pv)
    else:
      ls.insert(0,pv)
    i = i+1
  return ls

