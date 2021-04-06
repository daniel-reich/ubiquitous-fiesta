
def complete_factorization(num):
  div, lst = 2, []
  while not is_prime(num):
    if is_prime(div) and num % div == 0:
      lst.append(div)
      num = num//div
    else: div += 1
  lst.append(num)
  return lst
​
def is_prime(n):
  for i in range(2,n):
    if n % i==0: return False
  return True

