
def alternating_caps(txt):
  newS = ''
  i = True
  for char in txt:
    if i:
      newS += char.upper()
    else:
      newS += char.lower()
    if char != ' ':
      i = not i
  return newS

