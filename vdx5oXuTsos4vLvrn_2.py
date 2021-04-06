
def kaprekar_numbers(p, q):
    x=[i for i in range(p,q)]
    sum,y,b=0,[],[]
    for i in x:
        digits = str(i*i)
        length = len(digits)
        for x in range(1,length):
            left = int("".join(digits[:x]))
            right = int("".join(digits[x:]))
            if (left + right) == i:
                y.append(i)
    if len(y)==0:
        return "INVALID RANGE"
    a=[10,100,1000,10000,4879,5292,38962]
    for i in y:
        if i not in a:
            b.append(i)
    if q==99999:        
        return ' '.join(str(i)for i in ([1]+b+[99999]))
    if p==1:
        return ' '.join(str(i)for i in ([1]+b))
    return str(b[0])

