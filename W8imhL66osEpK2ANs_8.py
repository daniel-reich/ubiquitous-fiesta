
def time(dct, people, walls):
    r = dct['walls'] / dct['minutes'] / dct['people']
    
    t = walls / people / r
    
    return int(t)

