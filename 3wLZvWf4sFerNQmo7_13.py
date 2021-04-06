
def neutralise(st1,st2):
    zp = list(zip(st1,st2));st = ''
    for a,b in zp:
        if a+b == '--':
            st+='-'
        elif a+b == '++':
            st+='+'
        else:
            st+='0'
    return st

