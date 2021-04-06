
def fat_prime(a, b):
  if a > b:
    aux = a
    a = b
    b = aux
  for i in range(b,a-1,-1):
    counter_div = 0
    for d in range(2,int(i / 2) + 1):
      if i % d == 0:
        counter_div += 1
    if counter_div == 0:
      return i

