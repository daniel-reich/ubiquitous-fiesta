
def swap_xy(txt):
  a, b, c, d = map(int, txt.replace('(', '').replace(')', '').replace(' ', '').split(','))
  return str((b, a)) + ', ' + str((d, c))

