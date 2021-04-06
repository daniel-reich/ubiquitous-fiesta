
def hex_lattice(n):
    h = []
    for i in range(1,60):
        h.append(3*i**2-3*i+1)
​
    if n not in h:
        return 'Invalid'
    myans = []
    a = h.index(n)
    for i in range(a+1):
        myans.append((a-i+1)*' '+'o '*(a+i+1)+(a-i)*' '+'\n')
​
    x = ''
    for i in range(a+1):
        x += myans[i]
​
    for i in range(a-1,-1,-1):
        x += myans[i]
​
    return x[:-1]

