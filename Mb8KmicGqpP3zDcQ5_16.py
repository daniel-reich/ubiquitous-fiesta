
def josephus(n, i):
  ls=[]
  for j in range(1,n+1):
    ls.append(j)
  i -= 1
  position = i  
  while len(ls)>1:
    ls.pop(position)
    position =(position + i) % len(ls)
  return(ls[0])

