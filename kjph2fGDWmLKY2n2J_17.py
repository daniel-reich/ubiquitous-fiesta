
import re
COLOR = re.compile(r'rgba?\((\s*\d+%?)\s*,\s*(\d+%?)\s*,\s*(\d+%?)\s*,?\s*(\d*\.?\d+)?\s*\)$')
​
def valid_color (color):
    nopercent = lambda n: float(n[:-1])/100*255 if n[-1] == '%' else float(n)
    m = COLOR.match(color)
    if not m:
        return False
    if not all(m.groups()[:3]):
        return False
    nnn = tuple(map(nopercent, m.groups()[:3]))
    if ('rgba' in color) != bool(m.group(4)):
        return False
    if m.group(4) and not(0 <= float(m.group(4)) <= 1):
        return False
    return all(map(lambda c: 0<=int(c)<256, nnn))

