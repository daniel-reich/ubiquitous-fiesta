
def collatz(num):
  t=0
  while num>1:
    t+=1
    if num%2:
      num=num*3+1
    else:
      num/=2
  return t

