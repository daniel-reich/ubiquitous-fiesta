
def is_it_inside(folders,X,Y):
  step = X
  print(X)
  print(Y)
  print(folders)
  for i in range(len(folders)):
    if step == Y:
      result= True
      break
    else:
      result = False  
    for keys in folders:
      if step in folders[keys]:
        step = keys
        break
        print(step)
  print(result) 
  return result

