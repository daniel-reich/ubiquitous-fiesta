
def bacteria(final_mass):
    states = [(1, 1)]
    nights = 0
    proceed = True
    while proceed:
        nights += 1
        new_states = []
        for s in states:
            n, m = s[0], s[1] + 1
            if n * m < final_mass:
                new_states.append((n, m))
            else:
                return nights
            n, m = 2 * s[0], s[1] / 2 + 1
            if n * m < final_mass:
                new_states.append((n, m))
            else:
                return nights
        states = new_states
    return nights

