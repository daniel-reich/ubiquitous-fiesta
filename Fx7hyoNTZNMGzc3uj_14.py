
def number_len_sort(lst):
  L=[str(i) for i in lst]
  b=sorted(L, key = len) 
  return [int(i) for i in b]

