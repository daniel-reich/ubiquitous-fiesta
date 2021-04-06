
def simplify_sqrt(n):
  n = int(n)
  list = [1]
  for i in range(2,int(n/2)):
      if n%(i**2) == 0:
        list.append(i)
  a = int(max(list))
  b = int(n/(a**2))
  return (a,b)

