
def number_len_sort(lst):
  str_sort = sorted(map(str,lst),key=len);
  return list(map(int,str_sort));

