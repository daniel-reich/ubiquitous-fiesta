
def is_prime(num):
  div = []
  if num == 1:
    return False
  for i in range(1,num):
    t = num % i 
    if t == 0:
      div.append(i)
  size = len(div)
  return size<2

