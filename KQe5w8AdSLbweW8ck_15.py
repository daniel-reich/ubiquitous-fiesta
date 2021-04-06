
def char_at_pos(r, s):
  x = len(r)
  return r[1:x:2] if s == 'even' else r[0:x+1:2]

