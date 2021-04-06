
def third_most_expensive(dct):
    if len(dct) < 3:
        return False
    return sorted(dct, key=dct.get)[-3]

