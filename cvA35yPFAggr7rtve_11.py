
def last_ancestor(folders,X,Y):
  a = [X]
  b = [Y]
  for i in range(10):
      for key,value in folders.items():
          if X in value:
              a.append(key)
              X = key
          if Y in value:
              b.append(key)
              Y = key
  for j in a:
      if j in b:
          return j

