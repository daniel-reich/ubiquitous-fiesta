
def first_repeat(chars):
    for c in chars:
        if chars.count(c) > 1:
            return c
    return '-1'

