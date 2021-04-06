
def color_conversion(h):
    if type(h) == str:
        if h[0] == '#':
            h = h[1:]
        if len(h) != 6:
            return 'Invalid input!'
        for x in h:
            if x not in '0123456789abcdef':
                return 'Invalid input!'
        return {'r':int(h[:2], 16),
                'g':int(h[2:4], 16),
                'b':int(h[4:], 16)}
    z = [hex(x)[2:].zfill(2)
         for x in [h['r'], h['g'], h['b']]
         if 0 <= x <= 255]
    if len(z) != 3:
        return 'Invalid input!'
    return '#' + z[0] + z[1] + z[2]

