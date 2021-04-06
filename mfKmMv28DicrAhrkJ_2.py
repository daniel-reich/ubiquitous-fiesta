
def hex_color_mixer(colors):
    a = 0
    b = 0
    c = 0
​
    for i in range(len(colors)):
        a += int(colors[i][1:3],16)
        b += int(colors[i][3:5],16)
        c += int(colors[i][5:7],16)
​
    a = hex(round(a / len(colors)+.00001))[2:].upper().zfill(2)
    b = hex(round(b / len(colors)+.00001))[2:].upper().zfill(2)
    c = hex(round(c / len(colors)+.00001))[2:].upper().zfill(2)
​
    return '#'+str(a)+str(b)+str(c)

