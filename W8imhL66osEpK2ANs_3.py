
def time(dct, people, walls):
    m = dct["minutes"]
    w = dct["walls"]
    p = dct['people']
    rate = m / (w / p)
    return walls / people * rate

