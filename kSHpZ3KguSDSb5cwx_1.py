
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
c = ['0','1','2','3','4','5','6','7','8','9']
def dance_convert(pin):
    s = []
    for x in pin:
        if x not in c or len(pin) != 4:
            return 'Invalid input.'
    for x in range(len(pin)):
        y = moves[(int(pin[x]) + x) % 10]
        s.append(y)
    return s

