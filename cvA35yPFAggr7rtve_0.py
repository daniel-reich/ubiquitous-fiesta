
def last_ancestor(folders, X, Y):
  Fx,Fy=X,Y
  while not set(Fx)&set(Fy):
    for i in folders:
      if X in folders[i]:Fx+=i;X=i
      if Y in folders[i]:Fy+=i;Y=i
  return sorted(set(Fx)&set(Fy),key=Fx.index)[0]

