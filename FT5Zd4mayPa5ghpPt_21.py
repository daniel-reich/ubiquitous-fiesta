
import re
​
def color_conversion(h):
    if type(h) == str:
        h = h.replace('#', '')
        if re.match('[0-9abcdef]{6}$', h):
            return {'r': int(h[:2], 16), 'g': int(h[2:4], 16), 'b': int(h[4:], 16)}
        return 'Invalid input!'
    elif min(h.values()) >= 0 and max(h.values()) <= 255:
        return '#{:02x}{:02x}{:02x}'.format(h['r'], h['g'], h['b'])
    return 'Invalid input!'

