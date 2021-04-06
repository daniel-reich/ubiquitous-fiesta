
def how_mega_is_it(n):
    return 'not a mega milestone' if len(str(int(abs(n)))) < 3 else 'MEGA ' * (len(str(int(abs(n))))-2) + 'milestone'

