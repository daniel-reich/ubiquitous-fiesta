
def deep_count(lst):
  if lst == []:
    return 0
  else:
    if type(lst[0]) == list:
      return 1 + deep_count(lst[0]) + deep_count(lst[1:])
    else:
      return 1 + deep_count(lst[1:])

