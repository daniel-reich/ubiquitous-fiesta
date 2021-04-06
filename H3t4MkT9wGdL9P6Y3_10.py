
def oddish_or_evenish(num):
  sum = 0
  for ch in str(num):
    sum += int(ch)
  if sum % 2 == 0:
    return 'Evenish'
  else:
    return 'Oddish'

