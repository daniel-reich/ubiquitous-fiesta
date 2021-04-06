
def de_nest(lst):
  tmp = lst
  string=str(lst)
  for i in range(len(string)) :
    if (string[i]=="["):
      tmp = tmp[0]
    else:
      break
  return(tmp)

