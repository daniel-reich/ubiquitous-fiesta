
def match_last_item(lst):
  result = ''
  for item in lst[:-1]:
    result += str(item)
  return result == lst[-1]

