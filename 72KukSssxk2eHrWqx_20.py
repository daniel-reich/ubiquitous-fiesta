
def char_at_pos(r, s):
    if len(r) % 2 == 0:
        start = 0
    else:
        start = 1
    if s == 'even':
        return r[start::2]
    if s == 'odd':
        return r[abs(start-1)::2]

