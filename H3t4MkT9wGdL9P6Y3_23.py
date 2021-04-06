
def oddish_or_evenish(num):
  x = [int(x) for x in str(num)]
  return 'Evenish' if not sum(x) % 2 else 'Oddish'

