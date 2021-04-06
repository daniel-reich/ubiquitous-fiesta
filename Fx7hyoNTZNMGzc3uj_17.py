
def number_len_sort(lst):
  return [int(i) for i in sorted([str(i) for i in lst], key=len)]

