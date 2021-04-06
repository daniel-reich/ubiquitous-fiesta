
def power_ranger(power, minimum, maximum):
    i = 1
    d = 0
    while i ** power <= maximum:
        if i ** power >= minimum:
            d += 1
        i += 1
    return d

