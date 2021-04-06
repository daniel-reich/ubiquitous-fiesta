
def can_give_blood(donor, receiver):
  acompatibility = True
  bcompatibility = True
  rhcompatibility = True
  
  # Check for A
  if "A" in donor:
    acompatibility = "A" in receiver
  
  # Check for B
  if "B" in donor:
    bcompatibility = "B" in receiver
    
  # Check for Rh
  if "+" in donor:
    rhcompatibility = "+" in receiver
    
  return acompatibility and bcompatibility and rhcompatibility

