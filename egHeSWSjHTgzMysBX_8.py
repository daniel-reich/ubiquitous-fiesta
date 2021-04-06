
def half_a_fraction(fract):
    fract = list(map(lambda x:int(x), fract.split('/')))
    if (fract[0]) % 2 == 0:
        fract[0] = str(int(fract[0]/ 2))
    else:
        fract[1] = str(fract[1]* 2)
    fract = list(map(lambda x:str(x), fract))
    return '/'.join(fract)

