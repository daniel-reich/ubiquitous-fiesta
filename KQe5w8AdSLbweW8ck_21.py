
def char_at_pos(r, s):
  ntype = lambda x : "even" if x % 2 == 0 else "odd"
  rvalue = [ value for index, value in enumerate(r, start=1) if ntype(index) == s]
  if isinstance(r, list):
    return rvalue 
  else:
    return ''.join(rvalue)

