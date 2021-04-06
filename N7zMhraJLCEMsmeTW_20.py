
def min_swaps(string):
  case1, case2 = [], []
  for i in range(len(string)):
    case1.append(str(i % 2))
    case2.append(str(abs(i % 2 - 1)))
  swap1 = sum([a != b for a, b in zip(string, case1)])
  swap2 = sum([a != b for a, b in zip(string, case2)])
  return min([swap1, swap2])

