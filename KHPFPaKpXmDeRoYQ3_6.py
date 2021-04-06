
def check_score(s):
  d = {
    "#" : 5,
    "O" : 3,
    "X" : 1,
    "!" : -1,
    "!!" : -3,
    "!!!" : -5
  }
  if sum([sum([d[y] for y in x]) for x in s]) < 0: return 0 
  else : return sum([sum([d[y] for y in x]) for x in s])

