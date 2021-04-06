
def persistence(num):
    cnt = 0
    while len(str(num))>1:
        mult = 1
        for a in str(num):
            mult*=int(a)
        cnt+=1
        num = str(mult)
    return cnt

