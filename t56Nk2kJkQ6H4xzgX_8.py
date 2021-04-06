
def swap_xy(txt):
  new = [t[1::] if t[0] == '(' else t[:-1] for t in txt.split(', ')]
  return "({}, {}), ({}, {})".format(new[1],new[0],new[3],new[2])

