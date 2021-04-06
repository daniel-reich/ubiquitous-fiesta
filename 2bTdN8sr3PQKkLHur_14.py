
def divisible_by_b(a, b):
  while a > b:
    a+=1
    if a%b == 0:
      return a
      break

