
def can_give_blood(donor, receiver):
  if check_Antigen(donor, receiver) and check_RhFactor(donor, receiver):
    return True
  return False
  
def check_RhFactor(donor, receiver):
  if "+" in donor and "+" in receiver:
    return True
  elif "-" in donor:
    return True
  else:
    return False
    
def check_Antigen(donor, receiver):
  if "O" in donor:
    return True
  elif "AB" in donor and "AB" in receiver:
    return True
  elif "AB" in donor and "AB" not in receiver:
    return False
  elif "A" in donor and "A" in receiver:
    return True
  elif "B" in donor and "B" in receiver:
    return True
  else:
    return False

