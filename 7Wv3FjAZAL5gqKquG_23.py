
def era(er, ip):
    a=str((er/ip)*9)
    if len(a)<4:
        b=a.replace('.0','.00')
        return b
    else:
        return a[:4]

