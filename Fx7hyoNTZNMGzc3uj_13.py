
def number_len_sort(lst):
  strings = sorted([str(x) for x in lst], key=len)
  sort = [int(x) for x in strings]
  return sort

