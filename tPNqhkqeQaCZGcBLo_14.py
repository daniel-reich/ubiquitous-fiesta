
def determine_who_cursed_the_most(d):
  res = sum(x['me']-x['spouse'] for x in d.values())
  return 'ME!' if res > 0 else 'SPOUSE!' if res < 0 else 'DRAW!'

