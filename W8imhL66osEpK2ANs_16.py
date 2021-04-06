
def time(dct, people, walls):
    rate = (dct["walls"]/dct["people"])/dct["minutes"]
    return walls/people/rate

