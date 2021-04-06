
def char_at_pos(r, s):
  start = (s == 'even') == (len(r) % 2)
  return r[start::2]

