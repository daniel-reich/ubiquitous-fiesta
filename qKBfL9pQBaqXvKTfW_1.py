
def sum_of_slices(lst):
  s = 0
  arr = []
  for k in lst:
    if s+k <= 100:
      s+=k
    else:
      arr.append(s)
      s=k
  return arr + [k]*(k!=0)

