
def power_morphic(n):
    c = 0
    for i in range(2,11):
        if n == (n**i)%(10**len(str(n))):
            c += 1
    if c == 9:
        return "Polymorphic"
    elif c == 4:
        return "Quadrimorphic"
    elif c == 2:
        return "Dimorphic"
    elif c == 1:
        return "Enamorphic"
    else:
        return "Amorphic"

