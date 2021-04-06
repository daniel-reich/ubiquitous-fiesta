
def count_missing_nums(lst):
  k = []
  a = 0
  for index in lst:
    for c in index:
      if not 47 < ord(c) < 58:
        break
      else:
        a += 1 / len(index)
    else:
      k.append(int(index))
  return max(k) - min(k) - a + 1

