
def char_at_pos(r, s):
  if s=="even":
    return r[::-1][1::2][::-1]
  else:
    return r[::-1][0::2][::-1]

