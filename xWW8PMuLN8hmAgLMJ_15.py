
def postfix(expression):
    e=expression.split()
    while len(e)>1:
        for i in range(len(e)):
            if not str(e[i]).isnumeric() and len(str(e[i]))==1:
                x=eval(str(e[i-2])+str(e[i])+str(e[i-1]))
                e.pop(i)
                e.pop(i-1)
                e.pop(i-2)
                e.insert(i-2,x)
                break
    return int(e[0])

