
def collatz(num):
  i=0
  ct=0
  while num>1:
    if num%2==0:
      num = num/2
      ct += 1
    else:
      num = num*3 + 1
      ct += 1
  return ct

