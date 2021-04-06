
def cap_space(txt):
  return ''.join([ch if ch.islower() else ' ' + ch.lower() for ch in txt])

