
def upward_trend(lst):
  if any(type(i) == str for i in lst):
    return "Strings not permitted!"
  return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

