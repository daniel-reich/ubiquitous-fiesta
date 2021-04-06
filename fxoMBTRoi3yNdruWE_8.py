
def in_box(lst):
  for row in lst:
    if"*"in row and"*"not in row[0]and"*"not in row[-1]:
      return True
  return False

