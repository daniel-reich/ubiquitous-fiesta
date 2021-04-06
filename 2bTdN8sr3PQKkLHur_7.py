
def divisible_by_b(a, b):
  divisible = 0
  for i in range(a,a+b):
    if i > a and i > b:
      if i%b == 0:
        divisible += i
  return divisible

