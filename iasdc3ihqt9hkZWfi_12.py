
def can_give_blood(donor, receiver):
  return (donor[0:-1] in receiver[0:-1] or 'O' in donor[0:-1]) and (receiver[-1] == donor[-1] == '+' or donor[-1] =='-')

