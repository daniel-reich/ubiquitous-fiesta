
def arithmetic_operation(n):
    if n.endswith('/ 0'):
        return -1
    a, op, b = n.split()
    a, b = int(a), int(b)
    if op == '+':
        return a + b
    if op == '-':
        return a - b;
    if op == '*':
        return a * b
    return a // b

