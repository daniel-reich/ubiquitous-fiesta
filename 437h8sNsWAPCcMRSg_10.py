
def ss(a):
  f=True
  for i in range(2,a):
    if a%i==0:
      f=False
  if a==1:
    f=False
  return f
def product_of_primes(num):
  a=2
  while a<num:
    if ss(a):
      if num%a==0:
        if ss(int(num/a)):
          return True
          break
    a+=1
  if a==num:
    return(False)

