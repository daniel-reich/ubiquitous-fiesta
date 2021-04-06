
def match_last_item(lst):
  newList = ""
  last = lst[-1]
  lst = lst[:-1]
  for i in lst:
    newList += str(i)
  return newList == last

