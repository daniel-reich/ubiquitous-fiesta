
def check_score(s):
  s=sum({'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}[x]for y in s for x in y)
  return(s,0)[s<0]

