
def upward_trend(lst):
  try:
    return sorted(lst) == lst
  except:
    return "Strings not permitted!"

