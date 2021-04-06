
def calc_bundled_temp(n, temp):
    total = int(temp[:-2]) 
    for i in range(n):
        total += total * 0.1
    return str(round(total, 1)) + "*C"

