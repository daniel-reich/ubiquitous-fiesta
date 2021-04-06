
def check_score(s):
  d={'#' : 5,'O' : 3,'X' : 1,'!' : -1,'!!' : -3,'!!!' : -5}
  s=sum(s,[])
  A=[0]*len(s)
  for i in range(len(s)):
    A[i]=d[s[i]]
  if sum(A)<=0:
    return 0
  else:
    return sum(A)

