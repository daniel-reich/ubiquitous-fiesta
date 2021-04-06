
def collatz(num):
  i=0
  while num!=1:
    if num%2==0:
      num=num/2
    else:
      num=3*num+1
    i+=1
  return i

