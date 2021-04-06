
import numpy as np
def hex_color_mixer(colors):
    colors = [np.array(hex_to_int(color))+.1 for color in colors]
    mix = np.mean(colors, axis=0).round().astype(int)
    return '#{:02X}{:02X}{:02X}'.format(*mix)
​
def hex_to_int(hex_color):
    red = int(hex_color[1:3], 16)
    green = int(hex_color[3:5], 16)
    blue = int(hex_color[5:], 16)
    return (red, green, blue)

