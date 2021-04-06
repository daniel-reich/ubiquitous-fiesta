
def find(lst, item):
  try:
    x = lst.index(item)
  except ValueError:
    return -1
  else:
    return x
def advanced_sort(lst):
  unique_chars = []
  for item in lst:
    if find(unique_chars, item) == -1:
      unique_chars.append(item)
  sorted_lst = [[] for i in unique_chars]
  for item in lst:
    sorted_lst[find(unique_chars, item)].append(item)
  return sorted_lst

