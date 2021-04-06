
def fret_freq(g_str, fret):
    string_frequency={
        1: round(329.63,2),
        2: round(246.94,2),
        3: round(196),
        4: round(146.83,2),
        5: round(110),
        6: round(82.41,2)
    }
    for i in string_frequency:
        if g_str==i:
            return round(string_frequency[i]*2**(fret/12),2)

