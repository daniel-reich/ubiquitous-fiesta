
freq = [329.63, 246.94, 196.00, 146.83, 110.00, 82.41]
def fret_freq(g_str, fret):
  return round(freq[g_str-1] * 2**(fret/12), 2)

