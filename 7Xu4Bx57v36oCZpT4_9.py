
def where_is_waldo(lst):
  for idx, sub_list in enumerate(lst):
    if len(set(sub_list)) != 1:
      row = idx + 1
      break
  ch = [i for i in set(lst[row - 1]) if lst[row - 1].count(i) == 1][0]
  return [row, lst[row - 1].index(ch) + 1]

