
from math import floor
​
def _round(n):
    return floor(n) + 1 * (n % 1 >= 0.5)
​
def hex_color_mixer(colors):
    mixed = '#'
    colors = list(map(lambda c: c[1:], colors))
    for i in range(0, 6, 2):
        mixed += hex(_round(sum([int(color[i:i+2], 16) for color in colors])/len(colors)))[2:].zfill(2).upper()
    return mixed

