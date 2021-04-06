
def hex_color_mixer(lst: list) -> str:
    R, G, B = [], [], []
    for i in lst:
        R.append(int(str(i[1:3]), 16))
        G.append(int(str(i[3:5]), 16))
        B.append(int(str(i[5:7]), 16))
    colors = [R, G, B]
    mixed_color = '#'
    for i in colors:
        temp = str(hex(int(round(0.0000001 + sum(i) / len(i), 0))))[2:].upper()
        if len(temp) == 1:
            temp += '0'
        mixed_color += temp
    return mixed_color

