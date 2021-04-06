
def can_give_blood(donor, receiver):
  if donor[0] == 'O' or donor[0:-1] == receiver[0:-1] or len(receiver) > len(donor) and donor[0] == receiver[0]:
    if donor[-1] == '-' or donor[-1] == receiver[-1]:
      return True
  return False

