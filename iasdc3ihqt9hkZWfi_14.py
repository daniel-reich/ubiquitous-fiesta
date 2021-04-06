
def can_give_blood(donor, receiver):
  if donor == receiver:
    return True
  if donor == 'O-':
    return True
  elif donor == 'O+':
    if '+' in receiver:
      return True
    else:
      return False
  if len(donor) > len(receiver):
    return False
  anitgenA = False
  antigenB = False
  rhfactor = False
  AntigenA = False
  AntigenB = False
  Rhfactor = False
  for eachletter in donor:
    if eachletter == 'A':
      antigenA = True
    elif eachletter == 'B':
      antigenB = True
    elif eachletter == '-':
      rhfactor = True
  for eachletter in receiver:
    if eachletter == 'A':
      AntigenA = True
    elif eachletter == 'B':
      AntigenB = True
    elif eachletter == '+':
      Rhfactor = True
  if antigenA and AntigenA and rhfactor and Rhfactor:
    return True
  elif antigenA and AntigenA and not rhfactor and not Rhfactor:
    return True
  if antigenB and AntigenB and rhfactor and Rhfactor:
    return True
  elif antigenB and AntigenB and not rhfactor and not Rhfactor:
    return True
  else:
    return False

