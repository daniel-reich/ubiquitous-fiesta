
def loneliest_number(lo, hi):
  res = {'number':None, 'distance':0, 'closest':None}
  for i in range(lo,hi+1):
    l,h = i,i
    difference = 0
    while True:
      h+=1
      l-=1
      difference+=1
      if is_prime(h):
        if res['distance']<difference:
          res['number'] = i
          res['distance'] = difference
          res['closest'] = h
        break
      elif is_prime(l):
        if res['distance']<difference:
          res['number'] = i
          res['distance'] = difference
          res['closest'] = l
        break
  return res
      
def is_prime(n):
  if n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

