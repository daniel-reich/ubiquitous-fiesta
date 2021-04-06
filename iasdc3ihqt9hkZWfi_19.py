
def can_give_blood(donor, receiver):
  d_A, d_Rh = donor[:-1], donor[-1]
  r_A, r_Rh = receiver[:-1], receiver[-1]
  return (d_A == 'O' or d_A in r_A) and (d_Rh == '-' or d_Rh == r_Rh)

