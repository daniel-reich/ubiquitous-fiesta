
def diagonalize(n,d):
  l = list()
  
  if(d == "ul"):
    for i in range(n):
      a = list()
      for j in range(i, n+i):
        a.append(j)
      l.append(a)
​
  elif(d == "ur"):
    for i in range(n):
      a = list()
      for j in range(i, n+i):
        a.append(j)
      a = a[::-1]
      l.append(a)
​
  elif(d == "ll"):
    l = [0 for i in range(n)]
    for i in range(n):
      a = list()
      for j in range(i, n+i):
        a.append(j)
      
      l[-i+n-1] = a
​
  elif(d == "lr"):
    l = [0 for i in range(n)]
    for i in range(n):
      a = list()
      for j in range(i, n+i):
        a.append(j)
      a = a[::-1]
      l[-i+n-1] = a
​
  return l

