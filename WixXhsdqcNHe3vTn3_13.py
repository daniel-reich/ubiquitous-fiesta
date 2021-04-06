
def how_bad(n):
    lst = []
    l = str(bin(n)).count('1')
    p = bool([i for i in range(2,l) if l%i==0])
    if l%2==0:
        lst.append('Evil')
    else:
        lst.append('Odious')
    if p==False and l>1:
        lst.append('Pernicious')
    return lst

