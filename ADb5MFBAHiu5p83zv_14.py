
def fret_freq(g_str, fret):
  dct={1:329.63,2:246.94,3:196,4:146.83,5:110,6:82.41}
  return round(dct[g_str]*2**(fret/12),2)

