
def min_swaps(string):
  zero_one = "".join([str(x % 2) for x in range(len(string))])
  zero_result = 0
  one_result = 0
  for i in range(len(string)):
    if string[i] != zero_one[i]: zero_result += 1
    else: one_result += 1
  return min([zero_result, one_result])

