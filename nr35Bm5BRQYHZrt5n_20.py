
def upward_trend(lst):
  try:
    sorted(lst)
  except:
    return "Strings not permitted!"
  return sorted(lst)==lst

