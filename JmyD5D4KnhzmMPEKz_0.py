
def constraint(txt):
  if all(i in txt.lower() for i in 'abcdefghijklmnopqrstuvwxyz'):
    return 'Pangram'
  elif all(txt.lower().count(ch)==1 for ch in txt.lower() if ch != ' '):
    return 'Heterogram'
  elif len(set(i[0] for i in txt.lower().split())) == 1:
    return 'Tautogram'
  elif set.intersection(*map(set, txt.lower().split())):
    return 'Transgram'
  else:
    return 'Sentence'

