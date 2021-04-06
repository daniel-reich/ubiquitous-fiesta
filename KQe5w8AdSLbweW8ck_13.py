
def char_at_pos(r, s):
  func = lambda inpt : inpt[::2] if s == "odd" else inpt[1::2]
  return func(r)

