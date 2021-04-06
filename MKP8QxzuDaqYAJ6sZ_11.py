
def is_correct_aliases(names, aliases):
  for n in range(0,len(names)):
    a=names[n][0]
  return a==aliases[n][0] and a==aliases[n][aliases[n].find(' ')+1]

