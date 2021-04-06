
def series_resistance(lst):
    rt = sum(lst)
    return "{} ohm{}".format(rt, "s" if rt > 1 else "")

