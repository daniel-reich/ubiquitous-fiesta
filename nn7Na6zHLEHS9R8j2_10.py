
def deep_count(lst):
  element = 0
  for i in range(len(lst)):
    if isinstance(lst[i], list) == False:
      print(lst[i])
      element += 1
    if isinstance(lst[i], list):
      print(lst[i])
      element += 1
      element += deep_count(lst[i])
  return element

