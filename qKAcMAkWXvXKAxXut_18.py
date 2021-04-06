
def calc_bundled_temp(n, temp):
    f=int(temp[:-2])
    for i in range(n):
        f=f*1.1
    return str(round(f,1))+"*C"

