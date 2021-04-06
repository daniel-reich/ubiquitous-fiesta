
def RGB(hexa):
    return [int(hexa[i:i+2],16) for i in range(1, len(hexa), 2)]
    # hexa[0] = Red hexa[1] = Blue hexa[2] = Green
def hex_color_mixer(colors):
    import math
    Red,Green,Blue = [],[],[]
    for i in range(len(colors)):
        Red.append(RGB(colors[i])[0])
        Green.append(RGB(colors[i])[1])
        Blue.append(RGB(colors[i])[2])
​
    new_Red = round(sum(Red)/len(Red) + 0.01)
    new_Green = round(sum(Green)/len(Green) + 0.01)
    new_Blue = round(sum(Blue)/len(Blue) + 0.01)
    mixed = [new_Red,new_Green,new_Blue]
    for i in range(len(mixed)):
        x = hex(mixed[i])
        mixed[i] = x[x.index('x')+1:]
        mixed[i] = mixed[i].upper()
        if mixed[i] == "0":
            mixed[i] = "00"
​
    mixed.insert(0,"#")
​
    new_hexa = ''.join(mixed)
    return new_hexa

