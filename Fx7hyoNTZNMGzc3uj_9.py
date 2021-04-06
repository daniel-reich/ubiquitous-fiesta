
def number_len_sort(lst):
  lst_let = [str(i) for i in lst]
  lst_let.sort(key=len)
  lst_let = [int(i) for i in lst_let]
  return lst_let

