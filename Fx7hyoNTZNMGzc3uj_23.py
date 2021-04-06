
def number_len_sort(lst):
   
  return list(map(int, sorted(map(str, lst), key=len)))

