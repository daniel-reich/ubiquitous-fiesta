
def sort_by_string(lst, txt):
  return [item for char in txt for item in lst if item.startswith(char)]

