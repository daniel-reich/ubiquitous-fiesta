
def determine_who_cursed_the_most(d):
  m, s = 0, 0
  for key,value in d.items():
    for k1,v1 in value.items():
      if k1 == 'me':
        m += v1
      else:
        s += v1
  return 'DRAW!' if m == s else 'ME!' if m > s else 'SPOUSE!'

