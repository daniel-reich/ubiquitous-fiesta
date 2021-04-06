
def number_len_sort(lst):
  return list(map(int, sorted([str(x) for x in lst], key = len)))

