
def special_reverse(s, c):
  aux = list(s.split(" "))
  for n in range(len(aux)):
    if(aux[n].startswith(c)):
      aux[n] = aux[n][::-1]
  
  return " ".join(aux)

