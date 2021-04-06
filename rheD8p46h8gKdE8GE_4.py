
def grayscale(lst):
    greyscale = []
    for a in range(0,len(lst)):
        layer = []
        for row in range(0,len(lst[a])):
            for i in range(0,len(lst[a][row])):
                if lst[a][row][i] > 255:
                    lst[a][row][i] = 255
            if sum(lst[a][row]) < 0:
                layer.append([0,0,0])
            else:
                layer.append([round(sum(lst[a][row])/3),round(sum(lst[a][row])/3),round(sum(lst[a][row])/3)])
        greyscale.append(layer)
    return greyscale

