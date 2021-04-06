
def make_sandwich(i,f):
  sandwich = []
  for ingredient in i:
    if ingredient == f:
      sandwich += ['bread',ingredient,'bread']
    else:
      sandwich += [ingredient]
  return sandwich

