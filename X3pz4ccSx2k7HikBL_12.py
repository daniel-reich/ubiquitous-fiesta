
def showdown(p1, p2):
  p1_index = 0
  p2_index = 0
  for i in range(0, len(p1)):
    if p1[i] == "B":
      p1_index = i
    if p2[i] == "B":
      p2_index = i
  if p1_index < p2_index:
    return "p1"
  elif p2_index < p1_index:
    return "p2"
  else:
    return "tie"

