
def seq_level(lst):
  if lst[1]-lst[0] == lst[2]-lst[1]:
    return "Linear"
  elif lst[3] - (2*lst[2]) + lst[1] == lst[2] - (2*lst[1]) + lst[0]:
    return "Quadratic"
  else:
    return "Cubic"

