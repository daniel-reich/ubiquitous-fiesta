
def can_give_blood(donor, receiver):
  a1, rh1 = donor[:-1], donor[-1]
  a2, rh2 = receiver[:-1], receiver[-1]
  return (a1 == 'O' or a1 in a2) and rh1+rh2 != '+-'

