
def jazzify(lst):
  l = [element + "7" if element[-1]!="7" else element for element in lst]
  return l

