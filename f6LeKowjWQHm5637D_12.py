
def cap_to_front(s):
  up = ''
  low = ''
  for ch in s:
    if ch.isupper():
      up += ch
    else:
      low += ch
  return up + low

