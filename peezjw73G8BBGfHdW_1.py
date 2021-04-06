
def arithmetic_operation(n):
    a, op, b = n.split()
    if op == '+':
        return int(a) + int(b)
    if op == '-':
        return int(a) - int(b)
    if op == '*':
        return int(a) * int(b)
    if b == '0':
        return -1
    return int(a) // int(b)

