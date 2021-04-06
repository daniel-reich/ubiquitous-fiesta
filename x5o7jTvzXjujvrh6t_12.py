
def i_sqrt(n):
  i=0
  while n>=2:
    n **= .5
    i+=1
  return 'invalid' if n<0 else i

