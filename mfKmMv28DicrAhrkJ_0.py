
def hex_color_mixer(colors):
    r, g, b = [], [], []
    for color in colors:
        r.append(int(color[1:3], 16))
        g.append(int(color[3:5], 16))
        b.append(int(color[5:], 16))
​
    new_r = round(sum(r)/len(r) + 0.01)
    new_g = round(sum(g)/len(g) + 0.01)
    new_b = round(sum(b)/len(b) + 0.01)
    return '#{:02X}{:02X}{:02X}'.format(new_r, new_g, new_b)

