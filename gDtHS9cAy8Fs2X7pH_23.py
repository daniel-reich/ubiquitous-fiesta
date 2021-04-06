
def count_repetitions(lst):
  dic1 = {}
  for i in lst:
    if i not in dic1:
      dic1[i] = 1
    else:
      x = dic1[i]
      x += 1
      dic1[i] = x
  return dic1

