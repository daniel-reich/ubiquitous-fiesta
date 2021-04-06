
def how_mega_is_it(n):
    if abs(n) < 100:
        return 'not a mega milestone'
    megas = 'MEGA ' * ((str(abs(n)) + '.').index('.') - 2)
    return megas + 'milestone'

