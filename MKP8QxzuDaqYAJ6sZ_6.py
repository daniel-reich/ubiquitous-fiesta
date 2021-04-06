
def is_correct_aliases(names, aliases):
  for x, y in zip(names, aliases):
    if x[0] != y.split()[0][0] or x[0] != y.split()[1][0]:
      return False
  return True

