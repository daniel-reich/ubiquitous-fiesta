
def flash(f):
  return None if f[1] == '/' and f[2] == 0 else round(eval(''.join(map(str, f)).replace('x', '*')),2)

