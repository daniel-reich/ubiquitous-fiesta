
def fret_freq(g_str, fret):
  lst = [329.63,246.94,196.00,146.83,110.00,82.41]
  return float(format((lst[g_str-1]) * 2**(fret/12), '.2f'))

