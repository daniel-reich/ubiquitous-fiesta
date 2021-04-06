
def foil(length):
    d, e, pi = 4, 0.0025, 3.14159265359
    while length > 0:
        length -= pi*d; d += 2*e
    return round(d,4) if length > -(d-2*e)*pi/2 else round(d-e,4)

