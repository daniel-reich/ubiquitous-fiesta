
def is_correct_aliases(names, aliases):
  for i, x in enumerate(names):
    anon = aliases[i].split()
    if anon[0][0] != x[0] or anon[1][0] != x[0]:
      return False
    
  return True

