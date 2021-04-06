
def hex_color_mixer(c):
  if len(c) == 1: return c.pop()
  to_dec = lambda x: [int(x[i:i + 2], 16) for i in range(1, len(x), 2)]
  to_hex = lambda x: '#' + ''.join('{:02x}'.format(k) for k in x).upper()
  avg = lambda *x: int(round(sum(*x)/len(*x)+0.01, 0))
  return to_hex([avg([k[i] for k in [to_dec(x) for x in c]]) for i in range(3)])

