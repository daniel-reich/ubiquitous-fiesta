
def format_num(n):
  n_s = str(n)
  s_l = list(n_s)
  for i in range(len(s_l)-3, 0, -3):
    s_l.insert(i, ',')
  out = ''.join(s_l)
  return out

