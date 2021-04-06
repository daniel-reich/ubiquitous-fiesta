
def number_len_sort(lst):
  lst = sorted([str(i) for i in lst], key=len)
  return [int(i) for i in lst]

