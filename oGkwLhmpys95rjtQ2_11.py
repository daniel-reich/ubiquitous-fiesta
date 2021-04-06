
def match_last_item(lst):
  section = ""
  for x in range(len(lst) - 1):
    section += str(lst[x])
  return lst[-1] == section

