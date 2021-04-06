
def license_plate(s, n):
  plate = ''.join(list(reversed(s.replace('-', '').upper())))
  groups = len(plate) // n + (1 if len(plate) % n != 0 else 0)
  new_plate = ''
  for x in range(groups):
    new_plate += ('' if new_plate == '' else '-') + plate[n*(x):n*(x+1)]
  return ''.join(list(reversed(new_plate)))[:]

