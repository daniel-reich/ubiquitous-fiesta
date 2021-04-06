
def get_avg(sum_color, divisor):
    return round((sum_color)/divisor+.0001)
    
def get_rgb(hex_string):
    return int(hex_string[1:3], 16), int(hex_string[3:5], 16), int(hex_string[5:], 16)
​
def format_hex(color_int):
    hex_color = hex(color_int)[2:].upper()
    if len(hex_color) < 2:
        hex_color += '0'
    return hex_color
    
def hex_color_mixer(colors):
    new_r = 0
    new_g = 0
    new_b = 0
    color_count = 0
    for color in colors:
      color_count += 1
      r1,g1,b1 = get_rgb(color)
      new_r += r1
      new_g += g1
      new_b += b1
    
    r3 = get_avg(new_r, color_count)
    g3 = get_avg(new_g, color_count)
    b3 = get_avg(new_b, color_count)
    
    hex_r = format_hex(r3)
    hex_g = format_hex(g3)
    hex_b = format_hex(b3)
    
    new_hex = '#' + hex_r + hex_g + hex_b
    return new_hex

