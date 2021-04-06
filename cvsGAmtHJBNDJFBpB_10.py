
def can_traverse(x):
  heights = map(list, zip(*x))
  sums = [sum(height) for height in heights]
  return all(abs(sums[i] - sums[i+1]) <= 1 for i in range(len(sums)-1))

