
def staircase(n):
  return '\n'.join(['_'*(abs(n)-1-i)+'#'*(i+1) for i in range(abs(n))][::n//abs(n)])

