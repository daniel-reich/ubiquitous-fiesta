
def can_give_blood(donor, receiver):
  if 'A' in donor and 'A' not in receiver or 'B' in donor and 'B' not in receiver or '+' in donor and '+' not in receiver:
    return False
  return True

