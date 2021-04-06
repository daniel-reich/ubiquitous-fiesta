
def is_polygonal(n):
    if n == 1:
        return '0th of all'
    n2 = n - 1
    lst = []
    for x in range(3, n):
        if n2 % x == 0:
            x3 = n2 / x
            a = 0
            while x3 >= 1:
                a += 1
                x3 -= a
                if x3 == 0:
                    straw = str(a)
                    if straw[-1:] == '1':
                        asyntax = 'st'
                    elif straw == '2':
                        asyntax = 'nd'
                    elif straw == '3':
                        asyntax = 'rd'
                    else:
                        asyntax = 'th'
                    if len(straw) > 1:
                        if straw[-2:] == '11':
                            asyntax = 'th'
                    lst.append(straw + asyntax + ' ' + str(x) + '-gonal number')
    if lst == []:
        return False
    else:
        return lst

