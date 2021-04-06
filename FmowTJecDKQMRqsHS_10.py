
def crop_hydrated(field):
    for a in range(len(field)):
        for b in range(len(field[0])):
            if field[a][b] == "w":
                for c in range(-1, 2):
                    for d in range(-1, 2):
                        if 0 <= a + c < len(field) and 0 <= b + d < len(field[0]) and field[a + c][b + d] != "w":
                            field[a + c][b + d] = "#"
    return not any('c' in sublist for sublist in field)

