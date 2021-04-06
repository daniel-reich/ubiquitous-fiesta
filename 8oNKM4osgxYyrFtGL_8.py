
def multiply(l):
  ls = [] 
  for i in l:
    if type(i) == int:
      ls.append(list(map(int , list(str(i) * len(l)))))
    else:
      ls.append(list(str(i) * len(l)))
  return ls

