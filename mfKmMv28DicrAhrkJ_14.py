
def hex_color_mixer(colors):
    lc=len(colors)
    rc=.0000001
    red=green=blue=0
    for c in colors:
        red+=int(c[1:3],16)
        green+=int(c[3:5],16)
        blue+=int(c[5:7],16)
    red=hex(round(red/lc+rc))+'0'
    green=hex(round(green/lc+rc))+'0'
    blue=hex(round(blue/lc+rc))+'0'
    return ('#'+red[2:4]+green[2:4]+blue[2:4]).upper()

