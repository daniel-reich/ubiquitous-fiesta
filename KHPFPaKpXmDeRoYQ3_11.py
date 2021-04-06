
def check_score(s):
  strings = {'#': 5,'O': 3,'X':1,'!':-1,'!!':-3,'!!!': -5}
  score = sum(list(map(lambda x: sum(list(map(lambda y: strings[y],x))),s)))
  return score if score > 0 else 0

