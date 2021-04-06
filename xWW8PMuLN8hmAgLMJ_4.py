
def postfix(expression):
    t = expression.split(' ')
    op = ['+','-','*','/']
    
    while len(t) > 1:
        for i in range(len(t)-2):
            a = i
            b = a + 1
            c = b + 1
​
            if t[c] in op:
                if t[c] == '+':
                    t[a] = int(t[a]) + int(t[b])
                    del t[b]
                    del t[b] 
                elif t[c] == '-':
                    t[a] = int(t[a]) - int(t[b])
                    del t[b]
                    del t[b]
                elif t[c] == '*':
                    t[a] = int(t[a]) * int(t[b])
                    del t[b]
                    del t[b] 
                elif t[c] == '/':
                    t[a] = int(t[a]) // int(t[b])
                    del t[b]
                    del t[b]
                break    
    return t[0]

