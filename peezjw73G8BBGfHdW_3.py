
def arithmetic_operation(n):
    a, b, c = n.split()
    if b == '//' and c == '0':
        return -1
    if b == '+':
        return int(a) + int(c)
    elif b == '-':
        return int(a) - int(c)
    elif b == '*':
        return int(a) * int(c)
    else:
        return int(a) // int(c)

