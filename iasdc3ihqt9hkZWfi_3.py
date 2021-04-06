
def can_give_blood(donor, receiver):
  if "+" in donor and "-" in receiver:
    return False
  elif "O" in donor:
    return True
  elif "O" in receiver:
    return False
  elif "AB+" in receiver:
    return True
  elif "AB+" in donor:
    return False
  else:
    return donor[0] == receiver[0]

