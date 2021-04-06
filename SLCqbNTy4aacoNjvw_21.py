
def remove_dups(lst):
  result = []
  for i, item in enumerate(lst):
    if lst[:i].count(item) == 0:
      result.append(item)
  return result

