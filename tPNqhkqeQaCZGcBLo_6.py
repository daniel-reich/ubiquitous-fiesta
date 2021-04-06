
def determine_who_cursed_the_most(d):
    me, sp = 0,0
    for e in d:
        me, sp = me + d[e]["me"], sp + d[e]["spouse"]
    return "DRAW!" if me==sp else "ME!" if me>sp else "SPOUSE!"

