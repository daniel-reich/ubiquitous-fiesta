
def collatz(n):
  collatz_lst = []
  while(n > 1):
    if n%2 == 0:
      n = n//2
      collatz_lst.append(n)
    else:
      n = 3*n+ 1
      collatz_lst.append(n)
  collatz_lst.append(1)
  return (len(collatz_lst),max(collatz_lst))

