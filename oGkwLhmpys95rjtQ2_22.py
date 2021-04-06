
def match_last_item(lst):
  s = ""
  for e in lst[:-1]:
    s += str(e)
  return s == str(lst[-1])

