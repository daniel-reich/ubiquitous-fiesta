
def hex_lattice(n):
    i, h = 0, 1
    while h < n:
        i += 1
        h = h + (6 * i) - 6
    if h > n:
        return "Invalid"
    elif n == 1:
        return " o "
    add = (i + i - 1) * " o" + " \n"
    r = [add]
    for x in range(i - 1):
        add = add.replace("o", "", 1)
        add = add[::-1].replace(" ", "  ", 1)[::-1]
        r.insert(0, add)
        r.append(add)
    return "".join(r)[:-2] + " "

