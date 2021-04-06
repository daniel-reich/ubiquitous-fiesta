
def inverter(txt, type):
  txt = txt.split()
  if type == 'P':
    txt = txt[::-1]
  else:
    txt = [i[::-1] for i in txt]
  txt[0] = txt[0].title()
  txt[-1] = txt[-1].lower()
  return ' '.join(txt)

