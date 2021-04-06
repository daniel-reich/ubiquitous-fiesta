
def balanced(lst):
  mid = int(len(lst) / 2)
  if sum(lst[:mid]) > sum(lst[mid:]):
    return lst[:mid] * 2
  elif sum(lst[:mid]) < sum(lst[mid:]):
    return lst[mid:] * 2
  else:
    return lst

