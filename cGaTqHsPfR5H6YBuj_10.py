
def makeSandwich(i,f):
  new_lst = []
  for element in i:
    if element != f:
      new_lst.append(element)
    else:
      new_lst.append("bread")
      new_lst.append(element)
      new_lst.append("bread")
      
  return new_lst

