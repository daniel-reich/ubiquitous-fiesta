
def flick_switch(lst):
  lista = []
  boolean = True
  for item in lst:
    if item == "flick":
      if boolean == True: 
        boolean = False
      else:
        boolean = True
    lista.append(boolean)
  return lista

