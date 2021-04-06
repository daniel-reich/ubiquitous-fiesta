
def big_sub(lst):
  res = []
  for i in range(len(lst)):
    if lst[i] > 0:
      j = i + 1
      while j < len(lst)+1 and sum(lst[i:j]) > 0:
        res.append([sum(lst[i:j]), i, j - 1])
        j += 1
  return sorted(res, key=lambda x : (x[0], x[1]))[-1]

