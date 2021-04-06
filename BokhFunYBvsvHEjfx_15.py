
def seven_boom(lst):
  if any('7' in str(x) for x in lst):
    return "Boom!"
  return "there is no 7 in the list"

