
def twins(lst):
  S = sum(lst)
  s = 0
  for i in range(len(lst)):
    s += lst[i]
    if s == S // 2:
      return i+1

