
def alternating_caps(txt):
  u, ui = '', 0
  for i in txt:
    if i.isalpha():
      if ui == 0:
        u += i.upper()
      else:
        u += i.lower()
      ui = (ui + 1) % 2
    else:
      u += i
  return u

