
def determine_who_cursed_the_most(d):
    me, sp = 0, 0
    for rd, d1 in d.items():
        me += d1['me']
        sp += d1['spouse']
    if me > sp:     return 'ME!'
    if me < sp:     return 'SPOUSE!'
    return 'DRAW!'

