
def time(dct, people, walls):
    velocity = dct['minutes'] / dct['walls'] * dct['people']
    return (velocity / people) * walls

