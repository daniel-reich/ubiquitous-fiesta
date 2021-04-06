
def identify(*cube):
    a = sorted([len(i) for i in cube])
    if len(cube) * len(cube) != sum(a):
        if len(cube) * len(cube) - sum(a) < 0 and sum(a) == len(a) * a[0]:
            return 'Non-Full'
        else:
            return 'Missing {}'.format(abs(len(cube) * len(cube) - sum(a)))
    else:
        return 'Full'

