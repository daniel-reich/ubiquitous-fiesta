
def is_boiling(temp):
    dct = {'F': 212, 'C': 100}
    return int(temp[:-1]) >= dct[temp[-1]]

