
def hex_color_mixer(colors):
​
    def color_mixer(color_lst):
​
        mix = hex(round(sum([int(color, 16) for color in color_lst])/len(color_lst)+0.1)).lstrip("0x").upper()
        if mix:
            return mix
        else:
            return "00"
​
    r = color_mixer([color[1:3] for color in colors])
    g = color_mixer([color[3:5] for color in colors])
    b = color_mixer([color[5:7] for color in colors])
    return "#" + r + g + b

