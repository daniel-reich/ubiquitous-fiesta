
def fret_freq(g_str, fret):
  f = [329.63, 246.94, 196.00, 146.83, 110.00, 82.41] 
  freq = f[g_str-1] * 2**(fret/12)
  return round(freq, 2)

