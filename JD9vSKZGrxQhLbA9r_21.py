
def pile_of_cubes(m):
    cubes_counted = 0
    mass_remaining = m
    while mass_remaining > 0:
        cubes_counted += 1
        mass_remaining -= cubes_counted ** 3
    n = cubes_counted
    if mass_remaining == 0:
        return n
    return None

