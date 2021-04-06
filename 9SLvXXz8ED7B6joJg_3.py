
def lets_meet(distance, va, vb):
    seconds=(distance/(va+vb))*3600
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return '{}h {}min {}s'.format(int(h), int(m), int(s))

