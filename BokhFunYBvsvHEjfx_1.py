
def seven_boom(lst):
  if any("7" in str(i) for i in lst):
    return "Boom!"
  return "there is no 7 in the list"

