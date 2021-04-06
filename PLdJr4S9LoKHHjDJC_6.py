
def identify(*cube):
    l = len(sorted(cube, key=len)[-1])
    missing = 0
    for i in cube:
        if len(i) != l:
            missing += 1
    if missing > 0:
        return "Missing "+str(missing)
    elif len(cube) != len(cube[0]):
        return "Non-Full"
    return "Full"

