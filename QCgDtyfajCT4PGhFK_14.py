
def prime_factorization(num):
  x = 2
  lst = []
  while x <= num:
    if num%x==0:
      lst.append(x)
      num = num/x
    else:
      x += 1
  return lst

