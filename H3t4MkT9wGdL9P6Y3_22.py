
def oddish_or_evenish(num):
  digits = [int(i) for i in str(num)]
  if sum(digits) % 2 == 0:
    return 'Evenish'
  else:
    return 'Oddish'

