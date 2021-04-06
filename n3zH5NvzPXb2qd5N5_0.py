
def how_mega_is_it(n):
    m = len(str(abs(int(n))))
    if m < 3:
        return 'not a mega milestone'
    return '{} milestone'.format(' '.join(['MEGA']*(m-2)))

