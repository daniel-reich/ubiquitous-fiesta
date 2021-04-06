
def can_give_blood(donor, receiver):
  if donor == "O-":
    return True
  elif donor == receiver:
    return True
  else :
    arr = []
    if "A" in donor:
      arr.append("A" in receiver)
    if "B" in donor:
      arr.append("B" in receiver)
    if "+" in donor:
      arr.append("+" in receiver)
    return all(arr)

