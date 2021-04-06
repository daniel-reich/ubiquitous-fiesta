
def num_grid(lst):
    copy = []
    copy = lst
    counter = 0
    for x in range(len(lst)):
        for y in range(len(lst[0])):
            print("x = %i, y = %i" % (x,y))
            if lst[x][y] == "-":
                for addx in range(-1, 2, 1):
                    if x + addx not in range(0, len(lst)):
                        continue
                    for addy in range(-1, 2, 1):
                        if addx == 0 and addy == 0:
                            continue
                        if y + addy not in range(0, len(lst[0])):
                            continue
                        print(x+addx, y+addy)
                        if lst[x + addx][y + addy] == "#":
                            counter += 1
                        copy[x][y] = str(counter)
            counter = 0
    return copy

