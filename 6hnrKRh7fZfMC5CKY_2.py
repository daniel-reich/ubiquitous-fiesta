
def look_and_say(t):
  t = str(t)
  if not len(t)%2:
    return int(''.join(ch*int(n) for n, ch in zip(t[::2],t[1::2])))
  return 'invalid'

