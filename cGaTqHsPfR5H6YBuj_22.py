
def makeSandwich(i,f):
  ing_lst = []
  for ing in i:
    if f != ing:
      ing_lst.append(ing)
    else:
      ing_lst.extend(['bread',ing,'bread'])
  return ing_lst

