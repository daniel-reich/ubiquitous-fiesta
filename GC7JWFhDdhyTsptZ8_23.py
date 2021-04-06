
def sexy_primes(n, limit):
  res = []
  def isprime(x):
    flag=0
    for i in range(2,x):
      if x%i==0:
        flag=1
        break
    return True if flag==0 else False
  for i in range(2,limit):
    if isprime(i):
      if isprime(i+6) and (i+6<limit):
        if n==3:
          if isprime(i+12) and (i+12<limit):
            temp = (i,i+6,i+12)
            res.append(temp)
        else:
          temp = (i,i+6)
          res.append(temp)
  return res

