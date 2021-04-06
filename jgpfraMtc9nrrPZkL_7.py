
def switch_gravity_on(lst):
    return [list(i) for i in zip(*[sorted(i, reverse=True) for i in zip(*lst)])]

