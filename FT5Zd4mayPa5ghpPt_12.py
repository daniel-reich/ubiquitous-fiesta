
def color_conversion(h):
    if type(h) == str and (len(h) == 6 or (len(h) == 7 and h[0] == '#')):
        try:
            red, gr, blue = (int(h[-6: -4], 16), int(h[-4: -2], 16),
                             int(h[-2:], 16))
        except ValueError:
            return 'Invalid input!'
        if 0 <= red < 256 and 0 <= gr < 256 and 0 <= blue < 256:
            return {'r': red, 'g': gr, 'b': blue}
    elif type(h) == dict:
        if ('r' in h and 'g' in h and 'b' in h and len(h) == 3
                and 0 <= h['r'] < 256 and 0 <= h['g'] < 256
                and 0 <= h['b'] < 256):
            red, gr, blue = hex(h['r'])[2:], hex(h['g'])[2:], hex(h['b'])[2:]
            return '#{:0>2}{:0>2}{:0>2}'.format(red, gr, blue)
    return 'Invalid input!'

