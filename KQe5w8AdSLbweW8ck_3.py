
def char_at_pos(r,s):
  x = [v for i,v in enumerate(r) if i%2==["odd","even"].index(s)]
  return ''.join(x) if type(r)==str else x

