
def merge_sort(lst1, lst2):
  res = sorted(lst1+lst2)
  if lst1[0]>lst1[1]: return res[::-1]
  return res

