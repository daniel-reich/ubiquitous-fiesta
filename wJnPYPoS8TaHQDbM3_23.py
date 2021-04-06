
def dice_roll(n, outcome):
    x = 0
    if n == 6:
        for a in range(1,7):
            for b in range(1,7):
                for c in range(1,7):
                    for d in range(1,7):
                        for e in range(1,7):
                            for f in range(1,7):
                                if a+b+c+d+e+f == outcome:
                                    x += 1
    elif n == 5:
        for a in range(1,7):
            for b in range(1,7):
                for c in range(1,7):
                    for d in range(1,7):
                        for e in range(1,7):
                            if a+b+c+d+e == outcome:
                                x += 1
    elif n == 4:
        for a in range(1,7):
            for b in range(1,7):
                for c in range(1,7):
                    for d in range(1,7):
                        if a+b+c+d == outcome:
                            x += 1
    elif n == 3:
        for a in range(1,7):
            for b in range(1,7):
                for c in range(1,7):
                    if a+b+c == outcome:
                        x += 1
    elif n == 2:
        for a in range(1,7):
            for b in range(1,7):
                if a+b == outcome:
                    x += 1
    else:
        for a in range(1,7):
            if a == outcome:
                x += 1
    return x

