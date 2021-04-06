
def third_most_expensive(dct):
    if len(dct.keys()) < 3:
        return False
    return sorted(list(dct.items()), key=lambda x: -x[1])[2][0]

