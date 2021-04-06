
def sigilize(desire):
  unl1 = []
  for x in list(desire)[::-1]:
    if x not in unl1:
      unl1.append(x)
  l2 = ''
  for x in unl1:
    if x.capitalize() in 'QWRTYPSDFGHJKLZXCVBNM':
      l2 += x.capitalize()
  return l2[::-1]

