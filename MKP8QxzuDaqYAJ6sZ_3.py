
def is_correct_aliases(names, aliases):
  first_letter_of_names = [x[0]*2 for x in names]
  first_letter_of_aliases = [x.split()[0][0]+x.split()[1][0] for x in aliases]
  
  for i,j in zip(first_letter_of_names,first_letter_of_aliases):
    if i != j:
      return False
      break
  return True

