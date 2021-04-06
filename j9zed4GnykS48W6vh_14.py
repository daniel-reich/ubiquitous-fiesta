
def digits(number):
  p = 0
  l = 0
  while 10**p<number:
    l+=len(str(10**p))*(min(number,10**(p+1))-10**p)
    p+=1
  return l

