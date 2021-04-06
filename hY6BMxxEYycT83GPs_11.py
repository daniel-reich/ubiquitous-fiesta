
def multiply_by_11(n):
    n = '0'+n+'0'
    n = n[::-1]
    retnum = ''
    carry = 0
    for i in range(len(n)-1):
        summ = int(n[i]) + int(n[i+1]) + carry
        if summ >= 10:
            carry = int(str(summ)[0])
            summ = int(str(summ)[1])
        else:
            carry = 0
        retnum = str(summ) + retnum
    if carry == 1:
        retnum = '1'+retnum
    return retnum

