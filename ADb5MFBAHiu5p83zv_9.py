
def fret_freq(g_str, fret):
    frequencies = [329.63, 246.94, 196.00, 146.83, 110.00, 82.41]
    guitar = list(enumerate(frequencies, 1))
    for el in guitar:
        if el[0] == g_str:
            string = el
    frequencie = string[1] * (2 ** (fret/12))
    return round(frequencie, 2)

