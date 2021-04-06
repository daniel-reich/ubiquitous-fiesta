
def completely_filled(lst):
  return not any(i.isspace() for row in lst for i in row)

