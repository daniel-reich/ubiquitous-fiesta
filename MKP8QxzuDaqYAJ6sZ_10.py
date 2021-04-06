
def is_correct_aliases(names, aliases):
  for i in range(len(aliases)):
    j,k = aliases[i].split()
    if j[0] != k[0] or j[0] != names[i][0]:
      return False
  return True

