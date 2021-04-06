
def filter_primes(num):
  li=[]
  for i in num:
    if i>1:
      for j in range(2,i):
        if i%j==0:
          break
      else:
        li.append(i)
    else:
      continue
  return li

