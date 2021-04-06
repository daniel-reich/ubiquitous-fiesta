
def possibly_perfect(key, answers):
    z = []
    for x in range(len(key)):
        if key[x] == '_':
            continue
        if key[x] == answers[x]:
            z.append(True)
        else:
            z.append(False)
    return sum(z) == 0 or sum(z) == len(z)

