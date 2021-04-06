
def best_words(lst):
  d={'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':2,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
  currMx=-1
  resLst=[]
  for s in lst:
    score=0
    for c in s:
      score+=d[c.upper()]
    if score>currMx:
      currMx=score
      resLst=[s]
    elif score==currMx:
      resLst.append(s)
  return resLst

