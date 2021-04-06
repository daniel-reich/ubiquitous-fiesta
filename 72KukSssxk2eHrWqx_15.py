
def char_at_pos(r, s):
  if s == 'odd':
    r=r[-1::-2]
    return r[::-1]
  r=r[-2::-2]
  return r[::-1]

