
def arithmetic_operation(n):
    a = n.split()
    n1 = int(a[0])
    n2 = int(a[2])
    if a[1] == "+":
        return n1+n2
    if a[1] == "-":
        return n1-n2
    if a[1] == "*":
        return n1*n2
    if a[1] == "//" and n2 == 0:
        return -1
    if a[1] == "//" and n2 != 0:   
        return n1//n2

