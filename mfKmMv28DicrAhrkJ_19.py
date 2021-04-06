
def hex_color_mixer(colors):
    from math import ceil
    from math import floor
    def n_round(n):
        if n - floor(n) < 0.5:
            return floor(n)
        return ceil(n)
    lc = [(int(Z[1:3], 16), int(Z[3:5], 16), int(Z[5:7], 16)) for Z in colors]
    ar = hex(n_round(sum(Z[0] for Z in lc) / len(lc)))
    ag = hex(n_round(sum(Z[1] for Z in lc) / len(lc)))
    ab = hex(n_round(sum(Z[2] for Z in lc) / len(lc)))
    return ar.replace('0x', '#').zfill(2).upper() + \
           ag.replace('0x', '').zfill(2).upper() + \
           ab.replace('0x', '').zfill(2).upper()

