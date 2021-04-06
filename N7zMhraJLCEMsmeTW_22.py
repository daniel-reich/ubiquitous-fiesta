
def min_swaps(string):
  return min(sum([int(string[i])^(i%2) for i in range(len(string))]),sum([int(string[i])^(1-i%2) for i in range(len(string))]))

