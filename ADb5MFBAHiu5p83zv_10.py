
def fret_freq(g_str, fret):
  frequency = {1:329.63, 2:246.94, 3:196.00, 4:146.83, 5:110.00, 6:82.41}
  return round(frequency[g_str] * 2 ** (fret/12), 2)

