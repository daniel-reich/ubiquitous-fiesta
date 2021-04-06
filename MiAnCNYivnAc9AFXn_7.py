
def change_types(lst):
  print(lst)
  r=[]
  for el in lst:
    if type(el)==int:
      if el%2 ==0:
        r.append(el+1)
      else:
        r.append(el)
    elif type(el)== str:
      r.append(el.capitalize()+"!")
    else:
      r.append(not(el))
  return r

