
def XO(text):
  x = 0
  o = 0
  for ch in text:
    if ch in 'xX':
      x += 1
    elif ch in 'oO':
      o += 1
  if x == o:
    return True
  else:
    return False

