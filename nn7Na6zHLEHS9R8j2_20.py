
def deep_count(lst):
  counter = 0
  for i in lst:
    if type(i) == list:
      counter += deep_count(i)
    counter += 1
  return counter

