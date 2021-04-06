
def remove_leading_trailing(n):
    if "." in n:
        natural,decimal=n.split(sep='.')
    else:
        natural=n
        decimal=''
    while len(natural)>1 and natural[0]=='0':
        natural=natural[1:]
    while len(decimal)>=1 and decimal[-1]=='0':
        decimal=decimal[:-1]
    if not len(decimal) :
        return natural
    else:
        return natural+'.'+decimal

