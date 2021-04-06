
def char_at_pos(r, s):
  start = len(r)-1 if s == 'odd' else len(r)-2
  res = [r[i] for i in range(start,-1,-2)][::-1]
  return ''.join(res) if type(r) == str else res

