
def expanded_form(num):
    n1, n2 = str(num).split('.')
    p = len(n1)
    m1 = " + ".join(map(lambda i:
                    str(int(n1[i])*10**(p - i -1)),
                    filter(lambda i: int(n1[i]) !=0, range(p))))
    p = len(n2)
    m2 = " + ".join(map(lambda i:
                    str(int(n2[i])) + '/' + str(10**(i + 1)),
                    filter(lambda i: int(n2[i]) !=0, range(p))))
    if m1 and m2:
        return(m1 + " + " + m2)
    return(m1 + m2)

