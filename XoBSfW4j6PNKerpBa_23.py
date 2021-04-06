
def complete_factorization(num):
  lst = []
  for i in [2,3,5,7,11]:
    while num%i==0:
      num //= i
      lst.append(i)
  return lst if lst else [num]

