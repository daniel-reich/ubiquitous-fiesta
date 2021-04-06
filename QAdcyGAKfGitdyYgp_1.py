
def bacteria(final_mass):
    n = 1
    while 2**n - 1 < final_mass:
        n += 1
    return n if final_mass > 2**n - 1 else n - 1

