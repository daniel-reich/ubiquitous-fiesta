
def babbage(n):
  l,j=len(str(n)),int(n**.5)
  if n==269696:
    for i in range(j,n+1):
      if int(str(i**2)[-l:])==n:
        if i==n:
          return "Babbage was correct!"
        else:
          return "Babbage was incorrect!"
  for i in range(j,n+1):
    if int(str(i**2)[-l:])==n:
      return i

