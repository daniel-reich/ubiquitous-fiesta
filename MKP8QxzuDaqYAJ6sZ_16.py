
def is_correct_aliases(names, aliases):
  a = sum([1 for i in range(len(names)) if aliases[i].count(names[i][0]) == 2])
  return a == len(names)

