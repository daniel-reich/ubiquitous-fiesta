
def arithmetic_operation(n):
    d1,op,d2 = n.split()
    d1,d2 = int(d1),int(d2)
    if op=="+":
        return d1+d2
    elif op=="-":
        return d1-d2
    elif op=="*":
        return d1*d2
    else:
        if d2==0:
            return -1
        return d1//d2

