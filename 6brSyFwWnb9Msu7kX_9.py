
def pos_neg_sort(lst):
  new = []
  negativeIndex = {}
  for i,j in enumerate(lst):
    if j > 0:
      new.append(j)
      new.sort()
    else:
      negativeIndex[i] = j
  for key, value in negativeIndex.items():
    new.insert(key, value)
  return new

