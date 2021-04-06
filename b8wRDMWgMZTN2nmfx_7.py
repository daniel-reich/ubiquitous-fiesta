
def equal(a, b, c):
    if len({a, b, c}) == 3:
        return 0
    return 4 - len({a, b, c})

