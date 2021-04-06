
def worm_length(worm):
    return "{} mm.".format(10 * len(worm)) if len(set(worm)) == 1 else "invalid"

