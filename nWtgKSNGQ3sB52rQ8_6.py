
def evenly_divisible(a, b, c):
  divisible = []
  for i in range(a, b+1):
    if i % c == 0:
      divisible.append(i)
  count = 0
  for i in divisible:
    count+=i
  return count;

