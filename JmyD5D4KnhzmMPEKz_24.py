
def constraint(txt):
  if all(x in txt.lower() for x in 'abcdefghijklmnopqrstuvwxyz'):
    return 'Pangram'
  elif all(txt.lower().count(x)==1 for x in txt.lower() if x!=' '):
    return 'Heterogram'
  elif len(set(x[0] for x in txt.lower().split()))==1:
    return 'Tautogram'
  elif set.intersection(*map(set,txt.lower().split())):
    return 'Transgram'
  else:
    return 'Sentence'

