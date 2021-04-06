
def how_bad(n):
    myprimes = [2,3]
    for val in range(5,99999,2): 
        for j in range(2, int(val**.5)+1): 
            if (val % j) == 0: 
                break
            else: 
                myprimes.append(val)
    
    myans = []
    n = bin(n)[2:]
    c = 0
    for item in n:
        if item == '1':
            c += 1
    if c % 2 == 0:
        myans.append('Evil')
    else:
        myans.append('Odious')
    
    if c in myprimes:
        myans.append('Pernicious')
    
    return myans

