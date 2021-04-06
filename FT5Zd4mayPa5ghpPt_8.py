
def color_conversion(h):
    if isinstance(h, str):
        h = h[1:] if h[0] == '#' else h
        if any(x not in '#0123456789abcdef'for  x in h ) or len(h) > 6:
            return 'Invalid input!'
        else:
            values = {x: i for i, x in enumerate('0123456789abcdef')}
            t = list(zip(h, h[1:]))[::2]
            return {x: values[t[i][0]] * 16 + values[t[i][1]] for i, x in enumerate('rgb')}
    else:
        if any(x < 0 or x > 255 for x in h.values()):
            return 'Invalid input!'
        else:
            values = {i: x for i, x in enumerate('0123456789abcdef')}
            return ''.join(['#'] + [str(values[h[x] // 16]) + str(values[h[x]%16]) for x in 'rgb'])

