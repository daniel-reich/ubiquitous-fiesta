
def pi(n):
    m = 2
    t = 60
    x = 3 * 10 ** int(n * m)
    myans = 3
    for k in range(1,int(n*t)):
        x *= 2 * k - 1
        x //= 2 * k * 4
        myans += x // (2 * k + 1)
    return '3.1' + str(myans)[1:n]

