
def multiply_by_11(n):
    r = n[-1]
    reminder = 0
    n = '0'+n
    for i in range(1,len(n)):
        x = int(n[i*-1])+ int(n[(i+1)*-1])
        x += reminder
        if len(str(x)) > 1:
            r += str(x)[1]
            reminder = int(str(x)[0])
        else:
            r += str(x)
            reminder = 0
    return ((r+str(reminder))[::-1] if reminder else r[::-1])

