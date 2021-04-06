
def can_give_blood(donor, receiver):
  return all(e in receiver for e in donor if e in 'AB+')

