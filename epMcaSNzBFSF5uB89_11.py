
def currently_winning(scores):
  you=scores[::2]
  opp=scores[1::2]
  ans=[]
  for i in range(1,len(you)+1):
    a=sum(you[:i])-sum(opp[:i])
    if a==0:ans.append('T')
    elif a>0:ans.append('Y')
    else: ans.append('O')
  return ans

