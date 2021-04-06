
def collatz(n):
  lst = [n]
  while n != 1:
    if n%2==0:
      n = n/2
    else:
      n = n*3+1
    lst.append(n)
  return [len(lst)-1, max(lst)]

