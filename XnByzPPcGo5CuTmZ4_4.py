
def kix_code(addr):
    x = min([i for i in range(len(addr.split(',')[1])) if addr.split(',')[1][i].isdigit()])
    return addr.split(',')[-1].replace(' ','')[:6] + ''.join([i if i.isdigit() else (i.upper() if i.isalpha() else 'X') for i in addr.split(',')[1][x:]])

