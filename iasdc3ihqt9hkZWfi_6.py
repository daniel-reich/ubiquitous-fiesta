
def can_give_blood(donor, receiver):
  
  if (donor == "O-"):
    return True
  
  elif ("A" in donor) and ("A" not in receiver):
    return False
  
  elif ("B" in donor) and ("B" not in receiver):
    return False
  
  elif ("+" in donor) and ("+" not in receiver):
    return False
  
  else:
    return True

