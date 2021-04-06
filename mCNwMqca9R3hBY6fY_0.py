
def make_happy(s):
  for eye in ':8x;':
    s = s.replace(eye+'(',eye+')')
  return s

