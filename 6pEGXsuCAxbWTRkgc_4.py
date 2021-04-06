
def loves_me(n):
    if n == 1: return "LOVES ME"
    str = ["Loves me" if i % 2 == 0 else "Loves me not" for i in range(0, n)]
    str[-1] = str[-1].upper()
    return ", ".join(str)

