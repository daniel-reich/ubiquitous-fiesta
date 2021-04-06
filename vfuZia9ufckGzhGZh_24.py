
def seq_level(lst):
  L=[lst[i+1]-lst[i] for i in range(len(lst)-1)]
  if all(x==lst[1]-lst[0] and lst[1]-lst[0] for x in L):
    return  "Linear"
  elif seq_level(L)== "Linear":
    return "Quadratic"
  else:
    return "Cubic"

