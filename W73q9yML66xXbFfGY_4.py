
def coloured_triangle(a):
    length = len(a)
    if length==1:
        return a
    while (length>1):
        #print('in while',a)
        total = ''
        #print('length', length)
        for i in range(0, length-1):
            #print('in for',a)
            if a[i] != a[i+1]:
                if a[i]=='R':
                    if a[i+1]=='B':
                        total = total + 'G'
                        #print(total)
                    else:
                        total = total +'B'
                        #print(total)
                elif a[i]=='B':
                    if a[i+1]=='G':
                        total = total + 'R'
                        #print(total)
                    else:
                        total = total + 'G'
                        #print(total)
                else:
                    if a[i+1]=='B':
                        total = total + 'R'
                        #print(total)
                    else:
                        total = total +'B'
                        #print(total)
            else:
                total = total + a[i]
                #print(total)
        length = length-1
        a = total
        #print(a)
        #print('length', length)
    return a
​
print(coloured_triangle("RBR"))
print(coloured_triangle("RBRGBRB"))
print(coloured_triangle("B"))
print(coloured_triangle("GRGBG"))

