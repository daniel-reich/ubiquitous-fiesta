
def unique_lst(lst):
  result = []
  for i in lst:
    if i > 0 and i not in result:
      result.append(i)
  return result

