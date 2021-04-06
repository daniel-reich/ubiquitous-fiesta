
def rotate_by_one(lst):
  x = len(lst) - 1
  return lst[x:] + lst[:x]

