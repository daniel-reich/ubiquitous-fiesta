
def fret_freq(g_str, fret):
  f = [329.63, 246.94, 196, 146.83, 110, 82.41]
  return round(f[g_str-1]*2**(fret/12),2)

