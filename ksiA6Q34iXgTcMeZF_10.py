
def bonus(days):
  bonus_amounts, bonus = [0, 325, 550, 600], 0
  for i in range(0, days+1):
    if i > 48:
      bonus += bonus_amounts[3]
    if i >= 41 and i <= 48:
      bonus += bonus_amounts[2]
    if i > 32 and i <= 40:
      bonus += bonus_amounts[1]
  return bonus

