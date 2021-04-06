
def is_super_d(num):
    d= 2
    while True:
        n = d*num**d
        n = str(n)
        if str(d)*d in n:
            return "Super-{0} Number".format(d)
        d+=1
        if d>9:
            break
    return 'Normal Number'

