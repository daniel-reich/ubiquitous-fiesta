
def unmix(txt):
  return ''.join([ txt[x:x+2][::-1] for x in range(0, len(txt), 2) ])

