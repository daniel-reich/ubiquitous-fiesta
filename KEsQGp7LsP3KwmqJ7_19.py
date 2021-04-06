
def check(lst):
  index = lst.index(min(lst))
  if lst[index:] + lst[:index] == sorted(lst) and index:
    return "YES"
  else:
    return "NO"

