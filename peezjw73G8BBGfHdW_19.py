
def arithmetic_operation(n):
    op = {'+': lambda x, y: x + y,'-': lambda x, y: x - y,'*': lambda x, y: x * y,'//': lambda x, y: x // y,}
    container=n.split()
    if container[1] == "//" and container[-1]=="0":
        return -1
​
    return op[container[1]](int(container[0]),int(container[-1]))

