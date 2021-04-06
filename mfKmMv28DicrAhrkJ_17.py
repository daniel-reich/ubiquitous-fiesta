
from decimal import *
​
def get_chunks(iter, chunk_size):
    """Breaks an iterable into chunks of a given size"""
    return [iter[i:i+chunk_size] for i in range(0, len(iter), chunk_size)]
​
​
def sum_to_hex(s, num_elements):
    if s == 0:
        return "00"
    avg = int((Decimal(s) / Decimal(num_elements)).to_integral(ROUND_HALF_UP))
    converted = hex(avg)[2:].upper()
    return converted
​
​
def hex_color_mixer(colors):
    sum_r = 0
    sum_g = 0
    sum_b = 0
    num_colors = len(colors)
    for i in range(num_colors):
        r, g, b = get_chunks(colors[i][1:], 2)
        sum_r += int(r, 16)
        sum_g += int(g, 16)
        sum_b += int(b, 16)
    return "#" + sum_to_hex(sum_r, num_colors) + sum_to_hex(sum_g, num_colors) + sum_to_hex(sum_b, num_colors)

