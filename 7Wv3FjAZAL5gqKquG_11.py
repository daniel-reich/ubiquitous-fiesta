
def era(er, ip):
    dec = round(ip - round(ip),1)
    ip = ip-dec + dec*10/3
    return "{:.2f}".format(er/ip*9)

