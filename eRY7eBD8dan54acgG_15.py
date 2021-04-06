
def is_checkerboard(lst):
  for row in lst:
    pre = 1-row[0] #inverse
    for num in row:
      if num==pre:
        return False
      pre = num
  return True

