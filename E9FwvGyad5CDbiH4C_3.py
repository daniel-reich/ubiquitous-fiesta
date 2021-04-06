
def block(lst):
  return sum([(len(lst)-1-i) * row.count(2) for i, row in enumerate(lst)])

