
##  a(1)=1;a(n+1)=1+a(n+1-a(a(n)))}a(1) = 1; a(n+1) = 1 + a(n + 1 - a(a(n)))
def golomb(n):
  result = [1]
  nbr = 1
  while nbr <  n: 
    result.append( 1 + result[nbr  - result[result[nbr-1] - 1]])
    nbr = nbr + 1
  return result

