
def time(dct, people, walls):
    p, w, m = dct['people'], dct['walls'], dct['minutes']
    return (walls * m * p) // (people * w)

