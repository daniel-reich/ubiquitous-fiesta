
def replace_next_largest(lst):
  arr, brr = [], sorted(lst)
  for x in lst:
    if x == max(lst): arr.append(-1)
    else : arr.append(brr[brr.index(x)+1])
  return arr

