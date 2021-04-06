
def can_give_blood(donor, receiver):
  return not any(x in donor and x not in receiver for x in 'AB+')

