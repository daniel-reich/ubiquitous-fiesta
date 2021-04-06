
def is_polygonal(n):
    myans = []
    st = ['1']
    nd = ['2']
    rd = ['3']
    th = ['4','5','6','7','8','9','0']
​
    if n == 1:
        return '0th of all'
    if n < 4:
        return False
​
    for i in range(3,n):
        a = 1
        b = 1
        while b <= n:
            b += a*i
            if b == n:
                if len(str(a)) > 1 and str(a)[-2] == '1':
                    c = str(a)+'th'
                elif str(a)[-1] in st:
                    c = str(a)+'st'
                elif str(a)[-1] in nd:
                    c = str(a)+'nd'
                elif str(a)[-1] in rd:
                    c = str(a)+'rd'
                elif str(a)[-1] in th:
                    c = str(a)+'th'
                myans.append(c+' '+str(i)+'-gonal number')
            a += 1
​
    return myans

