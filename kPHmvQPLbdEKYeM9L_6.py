
def asteroid_collision(a):
    i = 0
    while i < len(a) - 1:
        if a[i] > 0 and a[i + 1] < 0:
            if a[i] > -a[i + 1]:
                a = a[:i + 1] + a[i + 2:]
            elif a[i] < -a[i + 1]:
                a = a[:i] + a[i + 1:]
            else:
                a = a[:i] + a[i + 2:]
            if i > 0:
                i -= 1
        else:
            i += 1
    return a

