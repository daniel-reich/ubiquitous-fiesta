
def is_checkerboard(lst):
  if all(a != b for row in lst for a,b in zip(row,row[1:]) ):
    lst = zip(*lst)
    return all(a != b for row in lst for a,b in zip(row,row[1:]) )
  return False

