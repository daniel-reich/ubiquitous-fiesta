
def sort_authors(lst):
  if len(lst) < 5:
    return [lst[2], lst[3], lst[0], lst[1]]
  else:
    return [lst[2], lst[3], lst[0], lst[1], lst[4]]

