
def widen_streets(lst, n):
  return [i.replace("  "," *").replace(" "," "*n).replace(" *","  ") for i in lst]

