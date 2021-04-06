
def truncatable(n):
  p = 0
  num = n//(10**p)
  right = True
  while num != 0:
    if right and not is_prime(num):
      right = False
    p += 1
    num = n//(10**p)
  num = n%(10**p)
  prev = None
  left = True
  while p > 0:
    if left and not is_prime(num):
      left = False
    p -= 1
    prev = num
    num = n%(10**p)
    if prev == num:
      return False
  if left and right:
    return "both"
  elif left:
    return "left"
  elif right:
    return "right"
  return False
    
def is_prime(num):
  for i in range(2,int(num**0.5)+1):
    if num%i == 0:
      return False
  return num > 1

