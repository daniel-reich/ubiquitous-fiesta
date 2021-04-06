
def can_give_blood(d, r):
  if d[-1] == r[-1] or d[-1] == "-":
    if d[:-1] in r[:-1] or d[:-1] == "O":
      return True
  return False

