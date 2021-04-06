
def can_give_blood(donor, receiver):
  if 'O' in donor:
    if '-' in donor:
      return True
    else:
      return '+' in receiver
  else:
    if '-' in donor:
      for i in donor[:-1]:
        if i not in receiver:
          return False
      return True
    else:
      for j in donor:
        if j not in receiver:
          return  False
      return True

