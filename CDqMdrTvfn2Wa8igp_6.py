
def next_element(lst):
  if len(lst) == 1:
    return lst[0]
  return lst[-1] + lst[-1] - lst[-2]

