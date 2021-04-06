
def rolls(lst):
  sum = 0
  good_luck_multiplier = 1
  for num in lst:
    roll = num
    roll*= good_luck_multiplier
    sum += roll
    good_luck_multiplier = 1
    if num == 1:
      good_luck_multiplier = 0
    elif num == 6:
      good_luck_multiplier = 2
  return sum

