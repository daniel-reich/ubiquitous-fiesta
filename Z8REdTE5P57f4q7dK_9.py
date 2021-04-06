
def get(n):
  if n%2:return n*3+1
  return n//2
  
def collatz(n):
  seq = []
  num=n
  counter=1
  while num!=1:
    nextnum = get(num)
    seq.append(nextnum)
    num = nextnum
    counter+=1
  return (counter, max(seq))

