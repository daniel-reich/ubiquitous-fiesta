
def pos_neg_sort(lst):
  result = []
  pos = sorted([i for i in lst if i > 0], reverse=True)
  for i in lst:
    if i > 0:
      result.append(pos.pop())
    else:
      result.append(i)
  return result

