
def primes_below_num(num):
  lst = [2]
  for i in range(3,num+1):
    l = []
    for j in range(2,i):
      l.append(i%j)
    if l.count(0) == 0:
      lst.append(i)
  return lst

