
def match_last_item(lst):
  return lst[-1] == ''.join([str(x) for x in lst[0:-1]])

