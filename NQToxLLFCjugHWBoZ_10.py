
def sort_by_character(lst, n):
  lst.sort(key = lambda test_list: test_list[n-1])
  return lst

