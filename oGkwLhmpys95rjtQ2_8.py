
def match_last_item(lst):
  if ''.join(str(x) for x in lst[:-1]) == lst[-1]:
    return True
  return False

