
def evenly_divisible(a, b, c):
  n = sum(num for num in range(a, b+1) if num % c == 0)
  return n

