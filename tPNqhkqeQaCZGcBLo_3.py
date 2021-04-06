
def determine_who_cursed_the_most(fight):
  total = 0
  for _round in fight.values():
    me, spouse = _round.values()
    total += me - spouse
  return 'ME!' if total > 0 else 'SPOUSE!' if total < 0 else 'DRAW!'

