
def percent_filled(box):
    flat = [item for row in box for item in row]
    o = flat.count('o')
    return str(round(o / (flat.count(' ') + o) * 100)) + '%'

