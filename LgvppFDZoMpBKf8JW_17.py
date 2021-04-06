
def digital_clock(seconds):
  h, k=divmod(seconds, 3600)
  m, l=divmod(k, 60)
  return '%02d:%02d:%02d'%(h%24,m,l)

