
def is_correct_aliases(names, aliases):
  m = list()
  for i,j in zip(names,aliases):
      m.append(int(j.count(i[0])/2))
      print(m)
  return all(m)

