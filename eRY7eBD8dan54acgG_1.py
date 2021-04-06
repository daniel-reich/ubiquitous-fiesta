
def is_checkerboard(lst):
  return lst==[i[::-1] for i in lst[::-1]]

