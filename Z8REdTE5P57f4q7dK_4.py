
def collatz(n):
  seq = []
  while n != 1:
    seq.append(n)
    if n%2==0:
      n = int(n/2)
    else:
      n=(n*3)+1
  return (len(seq)+1, max(seq))

