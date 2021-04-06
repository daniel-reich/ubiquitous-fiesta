
def unmix(txt):
  t = ''.join(sum([[j,i] for i, j in zip(txt[::2],txt[1::2])],[]))
  if len(txt) % 2:
    t += txt[-1]
  return t

