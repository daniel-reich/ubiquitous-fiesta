
def determine_who_cursed_the_most(D):
    count = lambda x: sum(D[d][x] for d in D)
    get_sign = lambda x: x and (-1 if x<0 else 1)
    check = get_sign(count('me') - count('spouse'))
    return ['DRAW!', 'ME!','SPOUSE!'][check]

