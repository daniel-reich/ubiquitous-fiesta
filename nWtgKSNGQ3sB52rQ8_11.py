
def evenly_divisible(a, b, c):
  nums = list(range(a, b + 1))
  sum = 0
  for i in nums:
    if i % c == 0:
      sum = sum + i
  return sum

