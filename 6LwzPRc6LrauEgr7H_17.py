
def worm_length(worm):
    if set(worm) != {'-'}:
        return 'invalid'
    return '{} mm.'.format(str(len(worm) * 10))

