
def sort_array(lst):
  result = []
  for i in range(len(lst)):
    result.append(min(lst))
    lst.remove(min(lst))
  return result

