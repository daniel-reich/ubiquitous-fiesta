
def win_round(you, opp):
  you=sorted(you)
  i=str(you.pop())
  j=str(you.pop())
  a=int(i+j)
  opp=sorted(opp)
  x=str(opp.pop())
  y=str(opp.pop())
  b=int(x+y)
  return True if a>b else False

