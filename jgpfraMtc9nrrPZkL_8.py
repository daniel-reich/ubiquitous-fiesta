
def switch_gravity_on(lst):
    return list(map(list, zip(*[sorted(col) for col in zip(*lst)])))[::-1]

