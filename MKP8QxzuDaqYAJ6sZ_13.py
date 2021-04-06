
def is_correct_aliases(names, aliases):
  return all(i[1].count(i[0][0]) == 2 for i in zip(names, aliases))

