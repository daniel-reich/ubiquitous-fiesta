
def percent_filled(box):
    s = ''.join(box)
    filled = s.count('o')
    return '{:.0%}'.format(filled/(filled + s.count(' ')))

