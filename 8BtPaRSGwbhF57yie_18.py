
def match_houses(step):
    if step < 1:
        return 0
    if step == 1:
        return 6
    else:
        return ((6 * step) - step) + 1

