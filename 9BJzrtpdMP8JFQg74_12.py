
def twins(lst):
  for i, n in enumerate(lst):
    if sum(lst[:i]) == sum(lst[i:]):
      return i

