
def is_correct_aliases(names, aliases):
  return all(i[0] == j.split()[0][0] == j.split()[1][0] for i, j in zip(names, aliases))

