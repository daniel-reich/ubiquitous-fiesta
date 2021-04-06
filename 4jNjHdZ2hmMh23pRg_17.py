
def cutting_grass(lst, *cuts):
  
  lista = []
  
  for cut in cuts:
    lst = [x - cut for x in lst]
    if min(lst) < 1:
      lista.append("Done")
    else:
      lista.append(lst)
      
  return lista

