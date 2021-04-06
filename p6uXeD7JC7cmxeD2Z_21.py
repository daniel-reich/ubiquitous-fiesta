
def calculate_score(games):
  def comp(a, b):
    if a + b in ["RS", "SP", "PR"]:
      return 1
    elif a + b in ["SR", "PS", "RP"]:
      return -1
    else:
      return 0
  v = 0
  for i in games:
    v = v + comp(i[0], i[1])
  if v == 0:
    return "Tie"
  elif v > 0:
    return "Abigail"
  else:
    return "Benson"

