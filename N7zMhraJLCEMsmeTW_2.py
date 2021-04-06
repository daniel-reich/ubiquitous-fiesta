
def min_swaps(string):
  target = ''.join(['1' if i % 2 == 0 else '0' for i in range(len(string))])
  swaps = sum([0 if target[i] == string[i] else 1 for i in range(len(string))])
  return min(swaps, len(string) - swaps)

