
def jazzify(lst):
  return [item + "7" if item[-1] != "7" else item for item in lst]

