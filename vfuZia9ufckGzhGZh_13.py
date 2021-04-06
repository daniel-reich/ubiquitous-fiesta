
def seq_level(lst):
  if lst[2]-lst[1]==lst[1]-lst[0]: return "Linear"
  if seq_level([a-b for a,b in zip(lst[1:],lst[:-1])]) == "Linear": return "Quadratic"
  return "Cubic"

