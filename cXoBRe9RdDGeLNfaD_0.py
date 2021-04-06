
def eight_bit(exp):
    r=range(-128,128)
    res=eval(exp)
    exl=exp.split()
    if res in r and int(exl[0]) in r and int(exl[2]) in r:
        b1=bin(int(exl[0]) & 255)[2:]
        b2=bin(int(exl[2]) & 255)[2:]
        bres=bin(res & 255)[2:]
        return (res,'{} {} {} = {}'.format(b1,exl[1],b2,bres))
    return 'Overflow'

