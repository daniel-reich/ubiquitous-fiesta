
def match_last_item(lst):
  return ''.join(str(lst[i]) for i in range(len(lst) - 1)) == lst[-1]

