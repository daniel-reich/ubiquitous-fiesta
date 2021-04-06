
def zero_indices(lst, k):
  longest = 0
  ans = []
  for i in range(len(lst)):
    temp = k
    run = 0
    indexes = []
    for x in range(i, len(lst)):
      if lst[x] == 1:
        run += 1
      elif temp > 0:
        run += 1
        temp -= 1
        indexes.append(x)
      else:
        break
    if run > longest:
      longest = run
      ans = indexes
  return ans

