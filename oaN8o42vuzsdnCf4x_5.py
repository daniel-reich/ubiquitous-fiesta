
def best_words(lst):
  dic={'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':2,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
​
  scores=[[w, sum([dic[l.upper()]  for l in w])] for w in lst]
  maxscore = max([item[1] for item in scores])
  return [w[0] for w in scores if w[1]==maxscore]

