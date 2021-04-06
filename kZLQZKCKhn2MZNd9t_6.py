
def possible_bonus(a, b):
  yes = False
  if b-a >= 1:
    if b-a <= 6:
      yes = True
    else:
      yes = False
  return yes

