
def sig_figs_int(n):
    while len(n) > 0 and n[0] == '0':
        n = n[1:]
    while len(n) > 0 and n[-1] == '0':
        n = n[:-1]
    return len(n)
​
def sig_figs_float(n):
    while len(n) > 0 and n[0] == '0':
        n = n [1:]
    if n[0] == '.':
        n = n[1:]
        while len(n) > 0 and n[0] == '0':
            n = n[1:]
        return len(n)
    return len(n) - 1
​
def sig_figs(num):
    num = num.replace('-', '')
    return sig_figs_int(num) if '.' not in num else sig_figs_float(num)

