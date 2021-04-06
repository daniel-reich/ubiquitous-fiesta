
def checkPrime(n):
    isPrime = True
    for j in range(2,int(n**.5)+1):
        if n % j == 0:
            return False
    return True
​
def bemirp(n):
    myans = ''
    l = len(str(n))
    non = ['2','3','4','5','7']
​
    #Check Prime
    if checkPrime(n):
        myans = 'P'
    else:
        return 'C'
    #Check Emirp
    nn = int(str(n)[::-1])
    if checkPrime(nn) and n != nn:
        myans = 'E'
    #Check Bemirp
    t = str(n)
    tt = str(nn)
    for item in t:
        if item in non:
            return myans
    nt = ''
    for item in t:
        if item == '6':
            nt += '9'
        elif item == '9':
            nt += '6'
        else:
            nt += item
​
    nnt = ''
    for item in tt:
        if item == '6':
            nnt += '9'
        elif item == '9':
            nnt += '6'
        else:
            nnt += item
​
    if checkPrime(int(nt)) and checkPrime(int(nnt)) and n != nn:
        myans = 'B'
​
​
    return myans

