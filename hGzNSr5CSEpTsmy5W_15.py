
def not_good_math(n, k):
  num=0
  while num<k:
    if str(n).endswith('0'):
      n=int(str(n)[:-1])
      num+=1
    else:
      n-=1
      num+=1
  return n

