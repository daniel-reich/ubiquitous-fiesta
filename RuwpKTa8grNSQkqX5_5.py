
def fractions(decimal):
    d = decimal.split('.')
    s = ['']*3
    s[0] = d[0]
    d = d[1].split('(')
    s[1] = d[0]
    d = d[1].split(')')
    s[2] = d[0]
    ln = len(s[0]) + len(s[1])
​
​
    cnt = 1
    while True:
        lt = ln + cnt*len(s[2])
        if(lt > 10): break
        cnt += 1
    st = s[0] + '.' + s[1] + s[2]*cnt
    flt = float(st)
    delta = '.' + '0'*9 + '9'
    fDelta = float(delta)
​
    print('DEC {}'.format(decimal))
    #print(delta)
​
    
​
    print('S {} FLT {}'.format(s, flt))
​
    res = []
​
    num = 1
    den = 2
    while True:
        val = float(num) / den
        d = abs(flt - val)
        #print('X {} {} {} {} {} {}'.format(val, flt, num, den, d, fDelta))
        if(abs(d) < fDelta):
            print('{} {} {}'.format(num, den, d))
            break
        if(val > flt):
            if(den % 1000 == 0):
                print('NUM {} DEN {}'.format(num, den))
            den += 1
            #num = 1
            num = int(flt * max(1, (den- 20)))
        else:
            num += 1
                        
    return str(num) + '/' + str(den)

