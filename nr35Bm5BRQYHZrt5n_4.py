
def upward_trend(lst):
  for i in lst:
    if type(i) is str:
      return "Strings not permitted!"
  sorted_list = sorted(lst)
  if lst == sorted_list:
      return True
  return False

