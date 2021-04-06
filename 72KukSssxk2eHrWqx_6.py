
def char_at_pos(r, s):
    return r[::-1][0::2][::-1] if s == 'odd' else r[::-1][1::2][::-1]

