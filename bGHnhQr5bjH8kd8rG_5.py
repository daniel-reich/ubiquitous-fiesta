
def rotate_by_one(lst):
  last_digit = lst.pop()
  lst.insert(0, last_digit)
  return lst

