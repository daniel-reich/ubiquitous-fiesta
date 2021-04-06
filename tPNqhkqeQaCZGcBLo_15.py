
def determine_who_cursed_the_most(d):
    me, spouse = 0, 0
    for r in d.values():
        me += r["me"]
        spouse += r["spouse"]
    return "DRAW!" if me == spouse else ("ME!" if me > spouse else "SPOUSE!")

