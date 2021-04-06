
def char_at_pos(r, s):
    return list(reversed(list(reversed(r))[::2])) if s == 'odd' and type(r) is list else list(reversed(list(reversed(r))[1::2])) if s == 'even' and type(r) is list else ''.join(list(reversed(list(reversed(r))[::2]))) if s == 'odd' and type(r) is str else ''.join(list(reversed(list(reversed(r))[1::2]))) if s == 'even' and type(r) is str else 0

