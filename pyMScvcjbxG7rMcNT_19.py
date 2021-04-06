
def sum_list(lst):
  total = 0
  for element in lst:
    if (type(element) == type([])):
      total += sum_list(element)
    else:
      total += element
  return total

