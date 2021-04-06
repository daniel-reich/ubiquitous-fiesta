
def swap_two(txt):
  if len(txt)<4: return txt
  r = ''
  while len(txt)>3:
    r += txt[2:4]
    r += txt[:2]
    txt = txt[4:]
  return r + txt

