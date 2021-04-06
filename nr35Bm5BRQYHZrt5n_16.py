
def upward_trend(lst): 
  if any(type(s) == str for s in lst):
    return "Strings not permitted!"
  return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

