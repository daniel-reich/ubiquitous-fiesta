
def inverter(s, t):
  s = s.lower().split(' ')
  s = ' '.join(s[::-1] if t == 'P' else [w[::-1] for w in s])
  return s[:1].upper() + s[1:]

