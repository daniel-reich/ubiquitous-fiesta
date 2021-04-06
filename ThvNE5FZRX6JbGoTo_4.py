
def inverter(txt, type):
  txt = txt.lower().split()
  if type == 'W':
    ret = [i[::-1] for i in txt]
  else:
    ret = txt[::-1]
  return ' '.join([ret[0].capitalize()]+ret[1:])

