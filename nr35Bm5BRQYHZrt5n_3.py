
def upward_trend(lst):
  return "Strings not permitted!" if [x for x in lst if type(x) == str] else sorted(lst) == lst

