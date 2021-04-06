
def bird_code(lst):
    names = []
    for bird in lst:
        cleanBird = bird.replace("-", " ").split()
        if len(cleanBird)== 1:
            name = cleanBird[0][:4]
        if len(cleanBird)== 2:
            name = cleanBird[0][:2] + cleanBird[1][:2]
        if len(cleanBird)== 3:
            name = cleanBird[0][0] + cleanBird[1][0] + cleanBird[2][:2]
        if len(cleanBird)== 4:
            name = cleanBird[0][0] + cleanBird[1][0] + cleanBird[2][0] + cleanBird[3][0]
        names += [name.upper()]
    return names

