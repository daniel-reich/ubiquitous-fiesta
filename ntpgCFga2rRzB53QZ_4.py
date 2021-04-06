
def staircase(n,i=1):
  if n<0: return '\n'.join(staircase(-n,i).split('\n')[::-1])
  return '_'*(n-i)+'#'*i+'\n'*(i<n)+staircase(n,i+1) if i<=n else ''

