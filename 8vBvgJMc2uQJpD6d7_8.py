
def prime_factors(num):
  num = int(num)
  lst = []
  while int(num)%2 == 0:
    lst.append(2)
    num = num/2
  for i in range(3, int(num*num)):
    if num == 1:
      break
    while num%i == 0:
      lst.append(i)
      num = num/i
  return lst

