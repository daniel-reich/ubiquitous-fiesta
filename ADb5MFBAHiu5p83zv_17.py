
def fret_freq(g_str, fret):
    fret = int(fret)
    stringFrequencies = [329.63,246.94,196.00,146.83,110.00,82.41]
​
    freq = float(stringFrequencies[g_str-1]) * (2**(fret/12))
    freq = round(float(freq),2)
    return freq

