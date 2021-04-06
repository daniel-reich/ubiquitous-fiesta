
def can_give_blood(donor, receiver):
  if "A" in donor and "A" not in receiver:
    return False
  if "B" in donor and "B" not in receiver:
    return False
  if donor[-1] == "+" and receiver[-1] != "+":
    return False
  return True

