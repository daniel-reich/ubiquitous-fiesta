
def upward_trend(lst):
  prev = 0
  for i in lst:
    if (isinstance(i, str)):
      return "Strings not permitted!"
    elif(i < prev):
      return False
    prev = i
  return True

