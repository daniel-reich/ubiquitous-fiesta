
import re
​
def hex_to_rgb(h):
    if not re.match(r'^#?[\da-f]{6}$', h):
        return 'Invalid input!'
    return {'r': int(h[-6:-4], 16), 'g': int(h[-4:-2], 16), 'b': int(h[-2:], 16)}
​
def rgb_to_hex(rgb):
    inRange = lambda c: 0 <= rgb[c] <= 255
    if not (inRange('r') and inRange('g') and inRange('b')):
        return 'Invalid input!'
    hexit = lambda n: hex(n+256)[-2:]
    return '#{}{}{}'.format(hexit(rgb['r']), hexit(rgb['g']), hexit(rgb['b']))
​
def color_conversion(h):
    return hex_to_rgb(h) if type(h) is str else rgb_to_hex(h)

