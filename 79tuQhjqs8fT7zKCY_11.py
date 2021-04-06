
def postfix(expr):
    vstack = []
    lis = expr.split()
    ops = set(["*", "+","/", "-"])
    for elem in lis:
        if elem in ops:
            b = vstack.pop()
            a = vstack.pop()
            
            if elem == "*":
                vstack.append(a*b)
            elif elem == "+":
                vstack.append(a+b)
            elif elem == "/":
                vstack.append(a/b)
            elif elem == "-":
                vstack.append(a-b)
            
            
        else:
            vstack.append(int(elem))
        print(vstack)
    return vstack[0]

