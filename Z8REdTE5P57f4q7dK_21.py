
def collatz(n):
  newlist = []
  newlist.append(n)
  while n!=1:
    if n%2==0:
      n = n/2
      newlist.append(n)
    else:
      n = (n*3)+1
      newlist.append(n)
  return (len(newlist),max(newlist))

