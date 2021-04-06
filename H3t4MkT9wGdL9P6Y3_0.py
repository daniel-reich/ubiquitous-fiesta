
def oddish_or_evenish(num):
  return 'Oddish' if sum(map(int, str(num))) % 2 else 'Evenish'

