
def match_last_item(lst):
  join = ""
  for l in range(0, len(lst) - 1):
    join += str(lst[l])
  last = lst[len(lst) - 1]
  if join == last:
    return True
  else:
    return False

