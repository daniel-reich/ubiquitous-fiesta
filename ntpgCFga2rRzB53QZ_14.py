
def staircase(n,l=0):
  if l+1==n and n>0:
    return '#'*n
  elif l+1==abs(n) and n<0:
    return ('_'*(l))+'#'
  if n>0:
    return ('_'*(n-l-1))+('#'*(l+1))+'\n'+staircase(n,l+1)
  else:
    return ('_'*l)+('#'*(abs(n)-l))+'\n'+staircase(n,l+1)

