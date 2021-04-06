
def char_at_pos(r, s):
  if s=="even":
    if len(r)%2:
      return r[1::2]
    else:
      return r[0::2]
  else:
    if len(r)%2:
      return r[0::2]
    else:
      return r[1::2]

