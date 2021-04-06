
def seq_level(lst):
  if lst[0] - lst[1] == lst[1] - lst[2]:
    return "Linear"
  elif lst[0] - 2 * lst[1] + lst[2] == lst[1] - 2 * lst[2] + lst[3]:
    return "Quadratic"
  else:
    return "Cubic"

