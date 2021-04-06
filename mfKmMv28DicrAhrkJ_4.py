
def hex_color_mixer(colors):
    res_color = [0, 0, 0]
    for c in colors:
        res_color[0] += int(c[1:3], 16)
        res_color[1] += int(c[3:5], 16)
        res_color[2] += int(c[5:], 16)
    for i in range(len(res_color)):
        res_color[i] = round(res_color[i] / len(colors) + 0.05)
    return '#' + ''.join(hex(c)[2:].upper() if len(hex(c)[2:]) > 1
                         else '0' + hex(c)[2:].upper()
                         for c in res_color)

