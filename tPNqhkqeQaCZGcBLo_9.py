
def determine_who_cursed_the_most(d):
    s = sum(d[k]["me"] - d[k]["spouse"] for k in d)
    return "ME!" if s > 0 else "SPOUSE!" if s < 0 else "DRAW!"

