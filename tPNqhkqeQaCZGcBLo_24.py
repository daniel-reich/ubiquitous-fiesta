
def determine_who_cursed_the_most(d):
  total = sum(dd.get('spouse') - dd.get('me') for dd in d.values())
  return 'DRAW!' if not total else 'SPOUSE!' if total > 0 else 'ME!'

