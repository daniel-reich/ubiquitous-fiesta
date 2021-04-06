
def how_bad(n):
    lst = []
    sum = 0
    while n != 0:
        sum += n%2
        n//=2
    if sum%2:
        lst.append('Odious')
    else:
        lst.append('Evil')
    if sum > 1:
        k = 0
        for i in range(2,sum):
            if sum%i==0:
                k = 1
        if k==0:
            lst.append('Pernicious')
    return lst

