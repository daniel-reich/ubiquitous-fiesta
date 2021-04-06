
def min_swaps(string):
  swaps1 = sum(string[i] == "1" if i % 2 == 0 else string[i] == "0" for i in range(len(string)))
  swaps2 = sum(string[i] == "0" if i % 2 == 0 else string[i] == "1" for i in range(len(string)))
  return min(swaps1, swaps2)

