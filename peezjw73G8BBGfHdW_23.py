
def arithmetic_operation(n):
​
    x = n.split(' ')
    
    if x[1] == '+':
        return int(x[0]) + int(x[2])
    
    elif x[1] == '-':
        return int(x[0]) - int(x[2])
    
    elif x[1] == '//':
        if x[2] == '0':
            return -1
        return int(x[0]) / int(x[2])
    
    elif x[1] == '*':
        return int(x[0]) * int(x[2])

