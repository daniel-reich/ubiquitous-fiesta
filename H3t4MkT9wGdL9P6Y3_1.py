
def oddish_or_evenish(num):
  return 'Oddish' if sum([int(x) for x in str(num)])%2 else 'Evenish'

