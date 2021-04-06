
def match_last_item(lst):
  return lst[-1] == ''.join(str(i) for i in lst[0:-1])

